from django import forms
from .models import person, bp_track
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password", "email" )


class RegisterForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ("f_name", "l_name", "phone","dob", "gender","height", "weight", "emer_name", "emer_phone", "emer_email", "emer_relation" )


class BPForm(forms.ModelForm):
    class Meta:
        model = bp_track
        fields = ("sys", "dia" )
