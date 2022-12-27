from django import forms
from django.forms import ModelForm

from .models import *


class MemberForm(ModelForm):
    class Meta:
        model  = Member
        fields = [ 'first_name', 'last_name', 'email' ]