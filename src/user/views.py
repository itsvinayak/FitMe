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
from FitMe import settings


########### register here #####################################
def TraineeRegister(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        Tform = TraineeRegisterForm(request.POST, request.FILES)
        if form.is_valid() and Tform.is_valid():
            user = form.save()
            profile = Tform.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            ######################### mail system ####################################
            htmly = get_template("user/Email.html")
            d = {"username": username}
            subject, from_email, to = (
                "welcome to FitMe",
                settings.EMAIL_HOST_USER,
                email,
            )
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

    return render(request, "user/register.html", {"form": form, "tform": Tform})


############################## TrainerRegister ###############################################


def TrainerRegister(request):
    # TrainerRegisterForm
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        Tform = TrainerRegisterForm(request.POST)
        if form.is_valid() and Tform.is_valid():
            user = form.save()
            profile = Tform.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            ######################### mail system ####################################
            htmly = get_template("user/Email.html")
            d = {"username": username}
            subject, from_email, to = (
                "welcome to FitMe",
                "settings.EMAIL_HOST_USER",
                email,
            )
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
        Tform = TrainerRegisterForm()

    return render(request, "user/register.html", {"form": form, "tform": Tform})


################################## update ####################################


@login_required
def TraineeProfileUpdate(request):
    if request.method == "POST":
        form = TraineeUpdateForm(request.POST,request.FILES,instance=request.user.trainee)
        print('\n\n\n\n\n-->',form.errors)
        if form.is_valid():
            form.save()
            messages.success(request, f"profile is updated")
            return redirect("TraineeProfile")

    form = TraineeUpdateForm(instance=request.user.trainee)

    data = {
        "form": form,
        "profile_pic": request.user.trainee.image.url,
        "title": "profile update for {}".format(request.user),
    }
    return render(request, "user/TraineeProfileUpdate.html", data)


############################## Trainee Profile #####################################


@login_required
def TraineeProfile(request):
    data = {"profile_pic": request.user.trainee.image.url}
    return render(request, "user/profile.html", data)
