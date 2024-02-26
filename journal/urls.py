from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('volume', views.volume, name="volume"),
    path('volume/<int:id>', views.volume_details, name="details"),
]
