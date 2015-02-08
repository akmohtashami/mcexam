from django.template.loader import render_to_string
from django.http import HttpResponse, Http404
from exams.utils import compile_tex
from tempfile import mkdtemp
import shutil
import re
from django.core.paginator import Paginator
from exams.models import ParticipantResult
from django.core.cache import cache
import os


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
        tmpl = re.sub(r'\n+', '\n', tmpl) #Remove double new lines

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