from django.shortcuts import get_object_or_404
from guardian.decorators import permission_required as guardian_permission_required
from django.contrib import messages
from exams.models import Exam
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.core.files import File
from tempfile import mkdtemp
from django.conf import settings
import subprocess
import os
import shutil


def build_tex_file(tex_file, output_directory, output_file_name, env=os.environ):
    compiler = subprocess.Popen(["xelatex", "-jobname=" + output_file_name], env=env, cwd=output_directory,
                                stdin=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE)
    return compiler.communicate(input=tex_file)


def get_env_exam_resource(exam):
    env = os.environ.copy()
    xelatex_path = getattr(settings, "XELATEX_BIN_PATH", None)
    if xelatex_path is not None:
        env["PATH"] = os.pathsep.join([xelatex_path, env["PATH"]])
    env["TEXINPUTS"] = exam.resources_dir + "//:"
    env["TTFONTS"] = exam.resources_dir + "//:"
    env["OPENTYPEFONTS"] = exam.resources_dir + "//:"
    return env

@guardian_permission_required("exams.change_exam", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def preview_statements(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    tex_file = exam.get_tex_file()
    tmp_folder = mkdtemp()
    output = build_tex_file(tex_file, tmp_folder, "statements", get_env_exam_resource(exam))
    try:
        statement_pdf_file = open(os.path.join(tmp_folder, "statements.pdf"))
        response = HttpResponse(statement_pdf_file.read(), content_type="application/pdf")
        statement_pdf_file.close()
    except IOError:
        response = HttpResponse(output, content_type="text/plain")
    shutil.rmtree(tmp_folder)
    return response

@guardian_permission_required("exams.change_exam", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def show_statements_tex(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    tex_file = exam.get_tex_file()
    return HttpResponse(tex_file, content_type="text/plain; charset=utf8")

@guardian_permission_required("exams.change_exam", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def publish_statements(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    tex_file = exam.get_tex_file()
    tmp_folder = mkdtemp()
    output = build_tex_file(tex_file, tmp_folder, "statements", get_env_exam_resource(exam))
    statements_path = os.path.join(tmp_folder, "statements.pdf")
    if os.path.isfile(statements_path):
        statements_file = open(statements_path, 'r')
        exam.statements_file.save('statements.pdf', File(statements_file))
        statements_file.close()
        messages.success(request, _("Statements were built successfully"))
        response = HttpResponseRedirect(reverse("exams:detail", kwargs={"exam_id": exam_id}))
    else:
        response = HttpResponse(output, content_type="text/plain")
    shutil.rmtree(tmp_folder)
    return response