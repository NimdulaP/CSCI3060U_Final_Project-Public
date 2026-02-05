from django.http import HttpResponse
from django.shortcuts import render

data = {
    'accounts': [
    {'id': 1, 'name': 'Account 1', 'balance': 1000},
    {'id': 2, 'name': 'Account 2', 'balance': 2500},
    {'id': 3, 'name': 'Account 3', 'balance': 500}
    ]
}

def homepage(request):
    return HttpResponse("Welcome to the homepage!")

def accounts(request):
    return render(request, 'accounts/accounts.html', data)