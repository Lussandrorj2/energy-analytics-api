from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import IntegrityError


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect("login")
            except IntegrityError:
                form.add_error(None, "Erro ao criar usuário. Tente outro username.")

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})