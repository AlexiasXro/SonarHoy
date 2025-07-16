from django import views
# from django.views import generic
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
class LoginView(views.View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'login.html', {})
