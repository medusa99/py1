from django.contrib import admin

# Register your models here.
#this displays question and choice on the admin page.
from . models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)
