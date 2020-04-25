from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class TraineeRegisterForm(ModelForm):
    class Meta:
        model = Trainee
        exclude = ("trainee", "user")


class TrainerRegisterForm(ModelForm):
    class Meta:
        model = Trainer
        fields = []


class TraineeUpdateForm(ModelForm):
    class Meta:
        model = Trainee
        exclude = ("trainee", "user")


class TrainerUpdateForm(ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
