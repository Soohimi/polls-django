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

admin.site.register(Question, QuestionAdmin)

