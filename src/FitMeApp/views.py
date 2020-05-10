from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from user.models import *
from .forms import *
from .models import *


##########################################################################################################


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            try:
                trainer = Trainer.objects.get(user=user)
            except:
                trainer = False
            if trainer:
                if trainer.approve:
                    login(request, user)
                    messages.success(request, f" wecome {username} !!")
                    try:
                        trainee = Trainee.objects.filter(trainer_ass=trainer)
                    except:
                        trainee = None
                    data = {"trainee": trainee}
                    return render(request, "TrainerDashBoard.html", data)
                else:
                    messages.success(
                        request, f" wecome {username} please ask admin to approve !!"
                    )
            else:
                login(request, user)
                try:
                    from src.user.models import Trainee

                    task = Task.objects.filter(
                        person=Trainee.objects.get(user=request.user)
                    )
                except:
                    task = None

                data = {"task": task}
                messages.success(request, f" wecome {username} !!")
                return render(request, "first.html")

        else:
            messages.info(request, f"account done not exit plz sign in")
    if request.user.is_anonymous:
        form = AuthenticationForm()
        return render(request, "index.html", {"form": form})
    else:
        try:
            trainer = Trainer.objects.get(user=request.user)
        except:
            trainer = False
        if trainer:
            if trainer.approve:
                try:
                    trainee = Trainee.objects.filter(trainer_ass=trainer)
                except:
                    trainee = None

                data = {"trainee": trainee}
                return render(request, "TrainerDashBoard.html", data)
            else:
                messages.success(
                    request, f" wecome {username} please ask admin to approve !!"
                )
        else:
            try:
                task = Task.objects.filter(
                    person=Trainee.objects.get(user=request.user)
                )
            except:
                task = None
            data = {"task": task}
            return render(request, "first.html", data)


######################################################################################################


@login_required
def giveTask(request, username):
    if request.method == "POST":
        form = TaskForm(request.POST)
        print(form.errors)
        if form.is_valid():
            trainee_here = Trainee.objects.get(user__username=username)
            note = request.POST["note"]
            task_to_give = request.POST["task_to_give"]
            Task.objects.create(
                person=trainee_here, note=note, task_to_give=task_to_give
            )
            messages.success(request, f"task given to user")

    form = TaskForm()
    data = {"form": form, "username": username}
    return render(request, "task.html", data)


@login_required
def seetask(request):
    data = {"task": Task.objects.filter(person=Trainee.objects.get(user=request.user))}
    return render(request, "seetask.html", data)


@login_required
def doneTask(request, id):
    Task.objects.get(id=id).task_complete = True
    data = {"task": Task.objects.filter(person=Trainee.objects.get(user=request.user))}
    return render(request, "seetask.html", data)


def about(request):
    return render(request, "about.html")


def portal(request):
    return render(request, "first.html")


def beginners_routines(request):
    return render(request, "beginners_routines.html")


def beginner_day1(request):
    return render(request, "beginner_day1.html")


def beginner_day2(request):
    return render(request, "beginner_day2.html")


def beginner_day3(request):
    return render(request, "beginner_day3.html")


def beginner_day4(request):
    return render(request, "beginner_day4.html")


def beginner_day5(request):
    return render(request, "beginner_day5.html")


def beginner_day6(request):
    return render(request, "beginner_day2.html")


def beginner_day7(request):
    return render(request, "beginner_day3.html")


def beginner_day8(request):
    return render(request, "beginner_day4.html")


def beginner_day9(request):
    return render(request, "beginner_day9.html")


def beginner_day10(request):
    return render(request, "beginner_day10.html")


def beginner_day11(request):
    return render(request, "beginner_day11.html")


def beginner_day12(request):
    return render(request, "beginner_day12.html")


def beginner_day13(request):
    return render(request, "beginner_day13.html")


def beginner_day14(request):
    return render(request, "beginner_day14.html")


def beginner_day15(request):
    return render(request, "beginner_day15.html")


def beginner_day16(request):
    return render(request, "beginner_day16.html")


def beginner_day17(request):
    return render(request, "beginner_day17.html")


def beginner_day18(request):
    return render(request, "beginner_day18.html")


def beginner_day19(request):
    return render(request, "beginner_day19.html")


def beginner_day20(request):
    return render(request, "beginner_day20.html")


def beginner_day21(request):
    return render(request, "beginner_day21.html")


def beginner_day22(request):
    return render(request, "beginner_day22.html")


def beginner_day23(request):
    return render(request, "beginner_day23.html")


def beginner_day24(request):
    return render(request, "beginner_day24.html")


def beginner_day25(request):
    return render(request, "beginner_day25.html")


def beginner_day26(request):
    return render(request, "beginner_day26.html")


def beginner_day27(request):
    return render(request, "beginner_day27.html")


def beginner_day28(request):
    return render(request, "beginner_day28.html")


def diet_beginner(request):
    return render(request, "diet_beginner.html")


def diet_intermediate(request):
    return render(request, "diet_intermediate.html")


def diet_hardcore(request):
    return render(request, "diet_hardcore.html")


def services(request):
    return render(request, "services.html")


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    return render(request, "contact.html")


def bmimetric(request):
    return render(request, "Fit.html")


def bmistandard(request):
    return render(request, "Standard.html")
