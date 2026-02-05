from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return HttpResponse("Welcome to the homepage!")

def accounts(request):
    return render(request, 'accounts/accounts.html', {'accounts': ['Account 1', 'Account 2', 'Account 3']})