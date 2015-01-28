from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from resources.models import Resource

# Register your models here.
class ResourceInLine(GenericTabularInline):
    model = Resource
    ct_field = 'owner_content_type'
    ct_fk_field = 'owner_object_id'

admin.site.register(Resource)