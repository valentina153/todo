from django.shortcuts import render, redirect, get_object_or_404
from .forms import toDoForm
from .models import todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def toDo(request):
    todos = todo.objects.filter(userID = request.user, datumZavrsetka__isnull = True).order_by('-važno')
    return render(request, 'toDoApp/todo.html', {'todos': todos})

@login_required
def noviTodo(request):
    if request.method == 'GET':
        return render(request, 'toDoApp/noviTodo.html', {'form': toDoForm()})
    else:
        form = toDoForm(request.POST)
        noviTodo = form.save(commit = False)
        noviTodo.userID = request.user
        noviTodo.save()
        return redirect('toDoApp:toDo')

@login_required
def zavrsi(request, todo_id):
    Todo = get_object_or_404(todo, pk = todo_id, userID = request.user)
    Todo.datumZavrsetka = timezone.now()
    Todo.save()
    return redirect('toDoApp:toDo')

@login_required
def uredi(request, todo_id):
    Todo = get_object_or_404(todo, pk = todo_id, userID = request.user)
    if request.method == 'GET':
        form = toDoForm(instance = Todo)
        return render(request, 'toDoApp/uredi.html', {'form': form})
    else:
        form = toDoForm(request.POST, instance = Todo)
        form.save()
        return redirect('toDoApp:toDo')

@login_required
def izbrisi(request, todo_id):
    Todo = get_object_or_404(todo, pk = todo_id, userID = request.user)
    Todo.delete()
    return redirect('toDoApp:toDo')

@login_required
def zavrseno(request):
    todos = todo.objects.filter(userID = request.user, datumZavrsetka__isnull = False).order_by('-datumZavrsetka')
    return render(request, 'toDoApp/zavrseno.html', {'todos': todos})