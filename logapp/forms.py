from django import forms
from logapp.models import lmode, userp
from django.contrib.auth.models import User


class uform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class lform(forms.ModelForm):
    class Meta():
        model = lmode
        fields = ('username','comment','pic_image')
