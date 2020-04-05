from django.core.exceptions import *
from django.http import HttpResponse
from datetime import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from user.models import Trainer


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if request.user.trainer :
                if request.user.trainer.approve:
                    login(request, user)
                    messages.success(request, f" wecome {username} !!")
                    return render(request, 'TrainerDashBoard.html', {'user': username})
                else:
                    messages.success(request, f" wecome {username} please ask admin to approve !!")
            else:
                login(request, user)
                messages.success(request, f" wecome {username} !!")
                return render(request, 'first.html', {'user': username})

        else:
            messages.info(request, f"account done not exit plz sign in")
    form = AuthenticationForm()
    return render(request, "index.html", {"form": form})


def about(request):
    return render(request, 'about.html')


def portal(request):
    return render(request, 'first.html')


def beginners_routines(request):
    return render(request, 'beginners_routines.html')


def beginner_day1(request):
    return render(request, 'beginner_day1.html')


def beginner_day2(request):
    return render(request, 'beginner_day2.html')


def beginner_day3(request):
    return render(request, 'beginner_day3.html')


def beginner_day4(request):
    return render(request, 'beginner_day4.html')


def beginner_day5(request):
    return render(request, 'beginner_day5.html')


def beginner_day6(request):
    return render(request, 'beginner_day2.html')


def beginner_day7(request):
    return render(request, 'beginner_day3.html')


def beginner_day8(request):
    return render(request, 'beginner_day4.html')


def beginner_day9(request):
    return render(request, 'beginner_day9.html')


def beginner_day10(request):
    return render(request, 'beginner_day10.html')


def beginner_day11(request):
    return render(request, 'beginner_day11.html')


def beginner_day12(request):
    return render(request, 'beginner_day12.html')


def beginner_day13(request):
    return render(request, 'beginner_day13.html')


def beginner_day14(request):
    return render(request, 'beginner_day14.html')


def beginner_day15(request):
    return render(request, 'beginner_day15.html')


def beginner_day16(request):
    return render(request, 'beginner_day16.html')


def beginner_day17(request):
    return render(request, 'beginner_day17.html')


def beginner_day18(request):
    return render(request, 'beginner_day18.html')


def beginner_day19(request):
    return render(request, 'beginner_day19.html')


def beginner_day20(request):
    return render(request, 'beginner_day20.html')


def beginner_day21(request):
    return render(request, 'beginner_day21.html')


def beginner_day22(request):
    return render(request, 'beginner_day22.html')


def beginner_day23(request):
    return render(request, 'beginner_day23.html')


def beginner_day24(request):
    return render(request, 'beginner_day24.html')


def beginner_day25(request):
    return render(request, 'beginner_day25.html')


def beginner_day26(request):
    return render(request, 'beginner_day26.html')


def beginner_day27(request):
    return render(request, 'beginner_day27.html')


def beginner_day28(request):
    return render(request, 'beginner_day28.html')


def diet_beginner(request):
    return render(request, 'diet_beginner.html')


def diet_intermediate(request):
    return render(request, 'diet_intermediate.html')


def diet_hardcore(request):
    return render(request, 'diet_hardcore.html')


def services(request):
    return render(request, 'services.html')


def mail(request):
    subject = "Greetings"
    msg = "Congratulations for your success"
    to = ['dharmsinghjmc@gmail.com', 'kaustubh2911@gmail.com']
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD, to)


def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')


def bmimetric(request):
    return render(request, 'Fit.html')


def bmistandard(request):
    return render(request, 'standard.html')
