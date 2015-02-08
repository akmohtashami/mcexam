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
from exams.utils import compile_tex
import os
import shutil

@guardian_permission_required("exams.change_exam", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def preview_statements(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    tex_file = exam.get_statements_tex_file()
    tmp_folder = mkdtemp()
    output = compile_tex(tex_file, tmp_folder, "statements", exam.add_tex_resources_to_environ())
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
    tex_file = exam.get_statements_tex_file()
    return HttpResponse(tex_file, content_type="text/plain; charset=utf8")

@guardian_permission_required("exams.change_exam", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def publish_statements(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    tex_file = exam.get_statements_tex_file()
    tmp_folder = mkdtemp()
    output = compile_tex(tex_file, tmp_folder, "statements", exam.add_tex_resources_to_environ())
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

@guardian_permission_required("exams.change_exam", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def all_result(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    for site in exam.examsite_set.all:
        #Add folder
        for user in site.member_set.all:
            pass
