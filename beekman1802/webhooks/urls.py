from django.urls import path

from . import views

urlpatterns = [
    path('aftership/', views.aftership)
]