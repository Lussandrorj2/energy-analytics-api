from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from .models import Cliente
from .serializers import ClienteSerializer
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


class ClienteViewSet(ModelViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['nome']

def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")

    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})