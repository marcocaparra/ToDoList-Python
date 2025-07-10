from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'), # Lista de tarefas
    path('nova/', views.nova_tarefa, name='nova_tarefa'), # Formulário para nova tarefa
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'), # Formulário para editar tarefa
    path('deletar/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'), # Confirmação de deleção
]