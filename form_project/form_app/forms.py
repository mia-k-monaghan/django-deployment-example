from django import forms
from django.contrib.auth.models import User
from form_app.models import Members,UserInfo

class SignUp(forms.ModelForm):
    class Meta:
        model = Members
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('profile_pic',)
