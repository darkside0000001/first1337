from django.shortcuts import render
from django.views.generic.base import View


class StartView(View):
    def get(self, request):
        return render(request, "test/11.html")

class Payyer(View):
    def get(self, request):
        return render(request, "payeer_1527118333.txt")

# Create your views here.
