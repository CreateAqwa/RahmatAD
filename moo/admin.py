from django.contrib import admin
from aqwa2 import view

from moo.models import aa as ADD_STUDENT
from moo.models import bb as CERTIFICATE

class aaAdmin(admin.ModelAdmin):
	list_display=("registrationno","name","fathername","mothername","mobno","city","message","gender","course","batchtime","Photo","fee","remaningfee")
admin.site.register(ADD_STUDENT,aaAdmin)

class bbAdmin(admin.ModelAdmin):
	list_display=("registrationno","name","fathername","mothername","mobno","city","message","gender","course","batchtime","Photo","fee","remaningfee")
admin.site.register(CERTIFICATE,bbAdmin)

