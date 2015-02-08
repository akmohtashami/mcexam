from django.db.models.signals import post_save
from django.dispatch import receiver
from exams.models import Question
from django.core.cache import cache

@receiver(post_save, sender=Question)
def invalidate_total_score_cache(sender, **kwargs):
    cache_name = "exam_" + str(kwargs["instance"].exam.id) + "_total_score"
    cache.delete(cache_name)

