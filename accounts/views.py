from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseBadRequest, HttpResponse
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == "GET":
        return render(request, "accounts/login.html")

    elif request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect("/shop/products/")

        return HttpResponseBadRequest("Invalid username or password.")


def logout_view(request):
    logout(request)
    return redirect("/shop/products/")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("/shop/products/")

    if request.method == "GET":
        return render(request, "accounts/register.html")

    elif request.method == "POST":
        try:
            password = request.POST.get("password", None)
            assert password, "Password is required"

            confirm = request.POST.get("confirm_password", None)
            assert confirm, "Confirm password is required"

            assert len(password) > 5 and password.isalnum(), "Password must be at least 6 characters long."
            assert password == confirm, "Passwords do not match."

            username = request.POST.get("username", None)
            assert username, "Username is required"

            User.objects.create_user(username=username, password=password)

            return HttpResponse("User has been created successfully !", status=201)

        except AssertionError as e:
            return HttpResponseBadRequest(e)

        except Exception as e:
            print(e)
            return HttpResponseBadRequest("Uncaught error ...")


@login_required
def profile_view(request):
    user = request.user

    if request.method == "GET":
        return render(request, "accounts/profile.html", {
            "user": user
        })

    elif request.method == "POST":
        username = request.POST.get("username", "")
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")

        if not username:
            return HttpResponseBadRequest("Username is required.")

        if User.objects.filter(username=username).exclude(pk=user.pk).exists():
            return HttpResponseBadRequest("Username is already taken.")

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return redirect("/account/profile/")
