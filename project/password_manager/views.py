from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User


@login_required(login_url="/login")
def index(request):
    
    # GET
    return render(request, "password_manager/index.html")


def login_view(request):
    
    # POST
    if request.method == "POST":

        # Authenticate the user
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            messages.error(request, "Invalid credentials.")
            return render(request, "password_manager/login.html")

    # GET
    else:
        return render(request, "password_manager/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):

    # POST
    if request.method == "POST":

        # Ensure that passwords match
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, "Passwords do not match!")
            return render(request, "password_manager/register.html")

        # Create new user
        username = request.POST["username"]
        email = request.POST["email"]
        try:
            user = User.objects.create_user(username, email, password)
            validate_password(password)
        except IntegrityError:
            messages.error(request, "Username already exists. Please use another username.")
            return render(request, "password_manager/register.html")
        except ValidationError as err:
            user.delete()
            return render(request, "password_manager/register.html", {
                "messages": err.messages
            })
            

        # Redirect to login
        return HttpResponseRedirect(reverse("login")) 

    # GET
    else:
        return render(request, "password_manager/register.html")