from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import subprocess


# Create your views here.

def LandingPage(request):
    print(request.user.is_authenticated, "----")
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'landing.html')


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def HomeDashboard(request):
    return render(request, 'dashboard/home.html')


@login_required(login_url='login')
def ContactsPage(request):
    return render(request, 'contacts.html')


@login_required(login_url='login')
def AboutPage(request):
    return render(request, 'about.html')


def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        email = request.POST.get('email')
        print(username, pass1, pass2, email)


        users = User.objects.all()
        for user in users:
            if user.username == username:
                print("Utilizador já existente")
                return render(request, 'signup.html', {"username_error": "Utilizador já existente"})
            if user.email == email:
                print("Email já existente")
                return render(request, 'signup.html', {"email_error": "Email já existente"})

        
        if pass1 == pass2:
            user = User.objects.create_user(username, email, pass1)
            user.save()
            return redirect('login')
        else:
            return render(request, 'signup.html', {"pass_error": "Palavras-passe não coincidem"})
    



    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)

        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'login.html', {"message": True})

    return render(request, 'login.html', {"message": False})


def LogoutPage(request):
    logout(request)
    return redirect('signup')


@login_required(login_url='login')
def OpenDoor(request):
    # Comando para executar o arquivo Python
    # Certifique-se de fornecer o caminho completo do arquivo se não estiver na mesma pasta da view.
    comando = "python exemplo.py"

    # Executa o comando usando o módulo subprocess
    resultado = subprocess.getoutput(comando)
    print(resultado)

    # Retorne o resultado como uma resposta HTTP
    return render(request, 'home.html')


@login_required(login_url='login')
def Settings(request):
    return render(request, 'settings.html')

@login_required(login_url='login')
def Profile(request):
    return render(request, 'home.html')

def Eletronica(request):
    return render(request, 'eletronica.html')

def Robotics(request):
    return render(request, 'robotics.html')


