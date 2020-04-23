from django.contrib import admin
from .models import Photo, PrivateDocument, Document

# Register your models here.
admin.site.register(Photo)
admin.site.register(PrivateDocument)
admin.site.register(Document)
