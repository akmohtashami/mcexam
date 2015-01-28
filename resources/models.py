from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext as _
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

# Create your models here.


def get_upload_path(instance, filename):
    if instance.is_private:
        base_folder = settings.PRIVATE_MEDIA_ROOT
    else:
        base_folder = settings.MEDIA_ROOT
    if len(instance.filename) != 0:
        filename = instance.filename
    if hasattr(instance.owner, 'resources_dir'):
        resource_dir = instance.owner.resources_dir
    else:
        resource_dir = os.path.join(instance.owner._meta.app_label, instance.owner._meta.module_name, str(instance.owner.pk))
    return os.path.join(base_folder, resource_dir, filename)


class Resource(models.Model):
    owner_content_type = models.ForeignKey(ContentType)
    owner_object_id = models.PositiveIntegerField()
    owner = GenericForeignKey('owner_content_type', 'owner_object_id')
    is_private = models.BooleanField(verbose_name=_("Private"), help_text=_("Private resources are not served by webserver"), default=True)
    filename = models.CharField(max_length=1000, verbose_name=_("File Name"), blank=True)
    resource = models.FileField(max_length=5000, upload_to=get_upload_path, storage=FileSystemStorage(location='/'))

    def save(self, *args, **kwargs):
        super(Resource, self).save(*args, **kwargs)
        if len(self.filename) == 0:
            self.filename = os.path.basename(self.resource.name)
        goal_file_name = get_upload_path(self, self.filename)
        if goal_file_name != self.resource.name:
            os.rename(self.resource.name, goal_file_name)
            self.resource.name = goal_file_name
        super(Resource, self).save(*args, **kwargs)
