from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

from .models import Tutorial


# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    # fields = ["tutorial_title", "tutorial_published", "tutorial_content"]

    fieldsets = [
        ("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]}),
    ]

    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}


admin.site.register(Tutorial, TutorialAdmin)
