from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about.html", views.index, name="index"),
    path("service.html", views.index, name="index"),
    path("team.html", views.index, name="index"),
    path('NetSuiteconnector/', views.NetSuiteconnector , name="NetSuiteconnector"),
]