from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('lodge', views.lodge),
    path('history', views.history),
    path('principles', views.principles),
]