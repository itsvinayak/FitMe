from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *
from django.contrib.auth.models import User

# for email send when register############################

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context



########### register here #####################################
def TraineeRegister(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        Tform = TraineeRegisterForm(request.POST)
        if form.is_valid() and Tform.is_valid():
            try:
                form.save()
                Tform.save()
            except:
                pass

            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            ######################### mail system ####################################
            htmly = get_template("user/Email.html")
            d = {"username": username}
            subject, from_email, to = "welcome to FitMe", "itssvinayak@gmail.com", email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except:
                print("email not working")
                pass
            ##################################################################
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("index")
    else:
        form = UserRegisterForm()
        Tform = TraineeRegisterForm()

    return render(request, "user/register.html", {"form": form,'tform':Tform})


############################## TrainerRegister ###############################################

def TrainerRegister(request):
    #TrainerRegisterForm
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        Tform = UserRegisterForm(request.POST)
        if form.is_valid() and Tform.is_valid():
            try:
                form.save()
                Tform.save()
            except:
                pass

            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            ######################### mail system ####################################
            htmly = get_template("user/Email.html")
            d = {"username": username}
            subject, from_email, to = "welcome to FitMe", "itssvinayak@gmail.com", email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except:
                print("email not working")
                pass
            ##################################################################
            messages.success(
                request, f"Your account has been created! ask admin to approve "
            )
            return redirect("index")
    else:
        form = UserRegisterForm()
        Tform = UserRegisterForm()

    return render(request, "user/register.html", {"form": form,'tform':Tform})

################################## upadte ####################################

def update(request):
    pass
