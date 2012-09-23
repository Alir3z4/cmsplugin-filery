from django.contrib import admin
from cmsplugin_filery.models import Image

class ImageInline(admin.TabularInline):
    model = Image
