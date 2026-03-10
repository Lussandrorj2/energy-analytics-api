from django.urls import path
from .views import consumo_page

urlpatterns = [

    path("", consumo_page, name="consumo"),

]