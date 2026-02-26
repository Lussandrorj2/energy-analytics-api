from django.urls import path
from .views import MediaConsumoView

urlpatterns = [
    path('media-consumo/', MediaConsumoView.as_view(), name='media-consumo'),
]