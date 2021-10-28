from django.shortcuts import render
from django.views.generic.base import View


class StartView(View):
    def get(self, request):
        return render(request, "test/11.html")

# Create your views here.
