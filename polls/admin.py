from django.contrib import admin
from .models import Question, Choice

from django.contrib import admin
from .models import Question

class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["publish_date"]})
    ]
    inlines=[ChoiceInLine]
    list_display = ["question_text", "publish_date", "was_published_recently"]

admin.site.register(Question, QuestionAdmin)

