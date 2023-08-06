from django.shortcuts import render, HttpResponse, redirect
from app1.models import User, Porta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import subprocess
from django.contrib.auth import update_session_auth_hash
import datetime




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
    registos_porta = Porta.objects.all().order_by('id')
    print(registos_porta)
    cooldown = False

    if len(registos_porta) > 0:
        ultimo_registo = registos_porta[len(registos_porta)-1]
        print(ultimo_registo)

        data = ultimo_registo.registo_hora.replace(tzinfo=None)
        print(data)

        now = datetime.datetime.now()
        print(now)
        diferenca = now - data
        diferenca_em_segundos = diferenca.total_seconds()
        print(f"Diferença total de segundos: {diferenca_em_segundos}")

        if diferenca_em_segundos < 5:
            cooldown = True

    if not cooldown:    
        porta = Porta.objects.create(utilizador=request.user)
        porta.save()
        
        comando = "python exemplo.py"

        # Executa o comando usando o módulo subprocess
        resultado = subprocess.getoutput(comando)
        print(resultado)

        # Retorne o resultado como uma resposta HTTP
        return render(request, 'porta.html', {"message": "Porta em cooldown!"})
    else:
        return render(request, 'porta.html', {"message": "Porta aberta com sucesso!"})


@login_required(login_url='login')
def Door(request):
    return render(request, 'porta.html')


@login_required(login_url='login')
def Settings(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        
        if form_type == 'form1':
            fname = request.POST.get('firstName')
            lname = request.POST.get('lastName')
            email = request.POST.get('email')

            print(fname, lname, email)

            user = request.user

            if fname != "" and fname != None and user.first_name != fname:
                user.first_name = fname

            if lname != "" and lname != None and user.last_name != lname:
                user.last_name = lname

            if email != "" and email != None and user.email != email:
                user.email = email

            user.save()

            return render(request, 'settings.html', {"message":"Sucesso!"}) 
        
        elif form_type == 'form2':
            #print("form2")
            current_password = request.POST.get('pass1')
            new_password = request.POST.get('pass2')
            new_password1 = request.POST.get('pass3')
            #print(current_password, new_password)
            
            user = request.user
            if user.check_password(current_password):
                if new_password == new_password1:
                    user.set_password(new_password)
                    user.save()
                    update_session_auth_hash(request, user)             
                    return render(request, 'settings.html', {"message2":"Sucesso!"}) 
                else:

                    return render(request, 'settings.html', {"message2":"Insucesso!"}) 
            else:
                return render(request, 'settings.html', {"message2":"Insucesso!"}) 
        
    return render(request, 'settings.html')


@login_required(login_url='login')
def Editar(request):
    user = request.user

    return render(request, 'settings.html')


@login_required(login_url='login')
def Profile(request):
    return render(request, 'profile.html')


def Eletronica(request):
    return render(request, 'eletronica.html')


def Robotics(request):
    return render(request, 'robotics.html')
