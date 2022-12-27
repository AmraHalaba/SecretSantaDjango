from django.contrib import admin

from .models import *


class MemberAdmin(admin.ModelAdmin):
    prepopulated_fields ={ 'slug' : ( 'first_name', 'last_name', ) }

admin.site.register(Member, MemberAdmin)