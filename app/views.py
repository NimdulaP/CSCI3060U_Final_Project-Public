from django.http import HttpResponse
from django.shortcuts import render, redirect

data = {
    'accounts': [
    {'id': 1, 'name': 'Account 1', 'balance': 1000},
    {'id': 2, 'name': 'Account 2', 'balance': 2500},
    {'id': 3, 'name': 'Account 3', 'balance': 500}
    ]
}

def lockscreen(request):
    if request.method == 'POST':
        return redirect('login')
    
    return render(request, 'lockscreen/lockscreen.html')

def login(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'admin':
            return redirect('accounts')

    return render(request, 'login/login.html')

def accounts(request):
    return render(request, 'accounts/accounts.html', data)