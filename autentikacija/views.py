from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.decorators import login_required

# Create your views here. 

def registracija(request):
    if request.method == 'GET':
        return render(request, 'autentikacija/registracija.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                validate_password(request.POST['password1'])
            except ValidationError as greska:
                return render(request, 'autentikacija/registracija.html', {'form': UserCreationForm(), 'greska': greska})
            try:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('toDoApp:toDo')
            except IntegrityError:
                return render(request, 'autentikacija/registracija.html', {'form': UserCreationForm(), 'greska': 'Korisničko ime je već zauzeto. Pokušajte ponovo.'})
        else:
            return render(request, 'autentikacija/registracija.html', {'form': UserCreationForm(), 'greska': 'Lozinke se ne podudaraju. Pokušajte ponovo.'})


def prijava(request):
    if request.method == 'GET':
        return render(request, 'autentikacija/prijava.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'autentikacija/prijava.html', {'form': AuthenticationForm(), 'greska': 'Korisničko ime i lozinka se ne podudaraju. Pokušajte ponovo.'})
        else:
            login(request, user)
            return redirect('toDoApp:toDo')

@login_required
def odjava(request):
    if request.method == 'POST':
        logout(request)
        return redirect('autentikacija:prijava')

