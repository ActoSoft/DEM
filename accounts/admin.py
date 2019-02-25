from django.contrib import admin
from .models import *

admin.site.register(Profile)
#admin.site.register(Group)

class GroupAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Group, GroupAdmin)