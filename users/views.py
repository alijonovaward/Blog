from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "Parollar mos kelmadi!")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username allaqachon mavjud!")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Ro‘yxatdan o‘tish muvaffaqiyatli!")
        return redirect("login")
    return render(request, "users/register.html")


def login_view(request):
    next_url = request.GET.get("next", "") or request.POST.get("next", "")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if next_url == "":
                next_url = "home"
            return redirect(next_url)  # 🔥 asosiy o‘zgarish
        else:
            messages.error(request, "Username yoki parol noto‘g‘ri!")

    return render(request, "users/login.html", {"next": next_url})


def logout_view(request):
    logout(request)
    return redirect("home")


def profile_view(request):
    return render(request, "users/profile.html")
