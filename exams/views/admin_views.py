from django.shortcuts import get_object_or_404, render
from guardian.decorators import permission_required as guardian_permission_required
from django.contrib import messages
from exams.models import Exam, ParticipantResult
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.core.files import File
from tempfile import mkdtemp
from exams.utils import compile_tex
from exams.views import shared_views
import os
import shutil
from django.core.cache import cache
import cStringIO
import zipfile

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
def all_site_results(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    exam_cache = "exam_" + str(exam_id) + "_result"
    if cache.get(exam_cache) is None:
        zip_result_file = cStringIO.StringIO()
        zip_result = zipfile.ZipFile(zip_result_file, "w")
        for site in exam.examsite_set.all():
            zip_result.writestr("%s.zip" % site.name, shared_views.get_site_result(exam, site))
        zip_result.close()
        cache.set(exam_cache, zip_result_file.getvalue())
    response = HttpResponse(cache.get(exam_cache), content_type="application/x-zip-compressed")
    response['Content-Disposition'] = 'attachment; filename=%s' % "results.zip"
    return response


@guardian_permission_required("exams.change_exam", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def full_ranking(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    context = {
        "exam": exam,
        "participants": exam.participantresult_set.all()
    }
    return render(request, "exams/base_templates/standings.html", context)