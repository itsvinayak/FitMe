from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name','password1', 'password2']

class TraineeRegisterForm(ModelForm):
    class Meta:
        model = Trainee
        fields = ['count_code','phone']

class TrainerRegisterForm(ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
