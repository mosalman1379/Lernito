from django.contrib import admin
from exam.models import Question,Quiz,Choices


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('quiz','question_name','correct')

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    pass