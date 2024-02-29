from django.contrib import admin

from .models import Module, Question 

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'module', 'correct']
    ordering = ['module']
# Register your models here.
class QuestionInlines(admin.StackedInline):
    model = Question


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display =['name','description', 'num_questions']
    inlines = [QuestionInlines]

#admin.site.register(Module)
#admin.site.register(Question, QuestionAdmin)