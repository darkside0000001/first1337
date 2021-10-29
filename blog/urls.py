from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.StartView.as_view()),
    path('payeer_1527118333.txt', views.Payyer.as_view()),
]