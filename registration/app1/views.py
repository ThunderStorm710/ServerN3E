from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import subprocess


# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

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

        if pass1 == pass2:
            user = User.objects.create_user(username, email, pass1)
            user.save()
            # return HttpResponse("User has been created successfully!!")
            return redirect('login')
        else:
            return HttpResponse("Data already used...")

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
            return HttpResponse("Username or password incorrect or not found")

    return render(request, 'login.html')


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

