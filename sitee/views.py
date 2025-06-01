from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            return render(request, 'form.html', {'error': 'Пользователь уже существует. Пожалуйста, войдите.',
                'show_login_link': True
            })

        user = User.objects.create_user(username=email, password=password)
        user.save()

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'form.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Неверный логин или пароль'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def home(request):
    return render(request, 'патренираваца.html')
# Create your views here.
