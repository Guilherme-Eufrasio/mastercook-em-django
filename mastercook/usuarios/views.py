from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.urls import reverse

Usuario = get_user_model()

def registrar_usuario(request):
    erro = None
    if request.method == "POST":
        nome = request.POST.get("inputNome")
        email = request.POST.get("inputEmail")
        password1 = request.POST.get("inputSenha")
        password2 = request.POST.get("inputRepitaSenha")

        if not nome or not email or not password1:
            erro = "Preencha todos os campos."
        elif password1 != password2:
            erro = "As senhas não conferem."
        elif Usuario.objects.filter(username=nome).exists():
            erro = "Esse nome de usuário já existe."
        else:
            user = Usuario.objects.create_user(
                username=nome,
                email=email,
                password=password1  # ✅ sem make_password
            )
            login(request, user)
            return redirect("home_area_restrita")  # leva para app área administrativa

    return render(request, "registro.html", {"erro": erro})


def login_usuario(request):
    erro = None
    if request.method == "POST":
        username = request.POST.get("usuarioUsername")  # ✅ vamos usar username
        password = request.POST.get("usuarioSenha")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home_area_restrita")  # vai para área restrita
        else:
            erro = "Usuário ou senha inválidos."

    return render(request, "logon.html", {"erro": erro})

def logout_usuario(request):
    request.session.flush()
    return redirect(reverse('home'))

# @login_required
# def area_restrita(request):
#     return render(request, "area_restrita.html")
# def home(request):
#     return render(request, 'logon.html')