from .models import *
from django.forms import ModelForm


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["note", "task_to_give"]
