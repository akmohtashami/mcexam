from django.template.loader import render_to_string
from exams.utils import compile_tex
from tempfile import mkdtemp
import shutil
import re
from django.core.paginator import Paginator
from exams.models import ParticipantResult
from django.core.cache import cache
import os
import cStringIO
import zipfile
from django.http import HttpResponseRedirect, HttpResponse, Http404


def get_user_result(exam, user):
    user_cache = "exam_" + str(exam.id) + "_user_" + str(user.id) + "_result"
    if cache.get(user_cache) is None:
        try:
            result = ParticipantResult.objects.get(exam=exam, user=user)
        except ParticipantResult.DoesNotExist:
            return None
        question_list = exam.get_user_question_details(user=user)
        question_columns = Paginator(question_list, exam.questions_per_column)
        question_columns_list = [question_columns.page(i) for i in question_columns.page_range]
        context = {
            "exam": exam,
            "user": user,
            "exam_data": result,
            "exam_question_columns": question_columns_list
        }
        tmpl = render_to_string("exams/base_templates/report_sheet.tex", context).encode("utf-8")
        tmpl = re.sub(r'\n+', '\n', tmpl) # Remove double new lines

        tmp_folder = mkdtemp()
        try:
            job_name = "result_" + str(exam.id) + "_" + str(user.id)
            compile_tex(tmpl, tmp_folder, job_name, exam.add_tex_resources_to_environ())
            statement_pdf_file = open(os.path.join(tmp_folder, job_name + ".pdf"))
            response = statement_pdf_file.read()
            statement_pdf_file.close()
        except Exception:
            response = None
        shutil.rmtree(tmp_folder)
        cache.set(user_cache, response)
    return cache.get(user_cache)

def get_key(exam):
    user_cache = "examkey_" + str(exam.id)
    if cache.get(user_cache) is None:
        question_list = exam.get_key_question_details()
        question_columns = Paginator(question_list, exam.questions_per_column)
        question_columns_list = [question_columns.page(i) for i in question_columns.page_range]
        context = {
            "exam": exam,
            "exam_question_columns": question_columns_list
        }
        tmpl = render_to_string("exams/base_templates/key_sheet.tex", context).encode("utf-8")
        tmpl = re.sub(r'\n+', '\n', tmpl) # Remove double new lines

        tmp_folder = mkdtemp()
        try:
            job_name = "key_" + str(exam.id)
            compile_tex(tmpl, tmp_folder, job_name, exam.add_tex_resources_to_environ())
            statement_pdf_file = open(os.path.join(tmp_folder, job_name + ".pdf"))
            response = statement_pdf_file.read()
            statement_pdf_file.close()
        except Exception:
            response = None
        shutil.rmtree(tmp_folder)
        cache.set(user_cache, response)
    return cache.get(user_cache)

def get_site_result(site):
    exam = site.exam
    site_cache = "exam_" + str(exam.id) + "_site_" + str(site.id) + "_result"
    if cache.get(site_cache) is None:
        zip_result_file = cStringIO.StringIO()
        zip_result = zipfile.ZipFile(zip_result_file, "w")
        for user in site.member_set.all():
            zip_result.writestr(user.get_full_english_name() + ".pdf", get_user_result(exam, user))
        zip_result.close()
        cache.set(site_cache, zip_result_file.getvalue())
    return cache.get(site_cache)
