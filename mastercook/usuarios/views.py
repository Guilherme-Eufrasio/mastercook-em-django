from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password



# Create your views here.

Usuario = get_user_model()


def registrar_usuario(request):
    erro = None
    print(request.POST.get("inputNome"))
    if request.method == "POST":
        nome = request.POST.get("inputNome")
        # username = request.POST.get("username")
        email = request.POST.get("inputEmail")
        password1 = request.POST.get("inputSenha")
        password2 = request.POST.get("inputRepitaSenha")
        # avatar = request.FILES.get("avatar")  # pega o arquivo
        # bio = request.POST.get("bio")

        # 🔹 validações manuais
        if not email or not password1:
            erro = "Preencha todos os campos."
        elif password1 != password2:
            erro = "As senhas não conferem."
        elif Usuario.objects.filter(email=email).exists():
            erro = "Esse nome de usuário já existe."
        else:
            # 🔹 cria o usuário
            user = Usuario.objects.create_user(
                apelido=nome,
                email=email,
                password=make_password(password1),
             )

       
            user.save()

            login(request, user)
            return redirect("area_restrita")

    return render(request, "registro.html", {"erro": erro})


def login_usuario(request):
    erro = None
    if request.method == "POST":
        email = request.POST.get("usuarioEmail")
        username = request.POST.get("usuarioUsername")

        password = request.POST.get("usuarioSenha")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("area_restrita")
        else:
            erro = "Usuário ou senha inválidos."

    return render(request, "logon.html", {"erro": erro})


def logout_usuario(request):
    logout(request)
    return redirect("login")


@login_required
def area_restrita(request):
    return render(request, "area_restrita.html")
def home(request):
    return render(request, 'logon.html')