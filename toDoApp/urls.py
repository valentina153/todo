from django.urls import path
from . import views

app_name = 'toDoApp'

urlpatterns = [
    path('', views.toDo, name = 'toDo'),
    path('novi', views.noviTodo, name = 'noviTodo'),
    path('zavrsi<int:todo_id>/', views.zavrsi, name = 'zavrsi'),
    path('uredi<int:todo_id>/', views.uredi, name = 'uredi'),
    path('izbrisi<int:todo_id>/', views.izbrisi, name = 'izbrisi'),
    path('zavrseno/', views.zavrseno, name = 'zavrseno'),
]
