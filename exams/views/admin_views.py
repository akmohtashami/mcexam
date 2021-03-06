from django.shortcuts import get_object_or_404, render
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
from exams.views import shared_views
import os
import shutil
from django.core.cache import cache
import cStringIO
import zipfile
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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

@guardian_permission_required("exams.see_all_results", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def all_site_results(request, exam_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    exam = get_object_or_404(Exam, id=exam_id)
    exam_cache = "exam_" + str(exam_id) + "_result"
    if cache.get(exam_cache) is None:
        zip_result_file = cStringIO.StringIO()
        zip_result = zipfile.ZipFile(zip_result_file, "w")
        for site in exam.examsite_set.all():
            zip_result.writestr("%s.zip" % site.name, shared_views.get_site_result(site))
        zip_result.close()
        cache.set(exam_cache, zip_result_file.getvalue())
    response = HttpResponse(cache.get(exam_cache), content_type="application/x-zip-compressed")
    response['Content-Disposition'] = 'attachment; filename=%s' % "results.zip"
    return response


@guardian_permission_required("exams.see_all_results", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def exam_key(request, exam_id):
	exam = get_object_or_404(Exam, id=exam_id)
	if not exam.check_implicit_permission(request.user, "view_results"):
		raise PermissionDenied
	result = shared_views.get_key(exam)
	if result is None:
		raise Http404
	else:
		return HttpResponse(result, content_type="application/pdf")
        
@guardian_permission_required("exams.see_all_results", (Exam, 'id', 'exam_id'), accept_global_perms=True, return_403=True)
def full_ranking(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    all_results = exam.participantresult_set.all()
    paginator = Paginator(all_results, 100)
    page = request.GET.get("page")
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    context = {
        "exam": exam,
        "participants": current_page
    }
    return render(request, "exams/base_templates/standings.html", context)
