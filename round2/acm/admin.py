from django.contrib import admin
from acm.models import *
# Register your models here.


class ExamplesInline(admin.TabularInline):
    model = Examples
    extra = 0


class QuestionsAdmin(admin.ModelAdmin):
    inlines = [ExamplesInline]

admin.site.register(UserProfile)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(McqQuestions)
admin.site.register(Submissions)
admin.site.register(McqSubmissions)