from django.urls import path

from . import views

app_name="invest"
urlpatterns = [

    path('', views.home, name="home"),
]