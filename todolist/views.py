from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm
# Create your views here.
def lista_tarefas(request): # Listar tarefas
    tarefas = Tarefa.objects.all() # Busca todas as tarefas
    return render(request, "lista.html", {"tarefas": tarefas}) # Renderiza a lista de tarefas

def nova_tarefa(request): # Criar nova tarefa
    if request.method == "POST": # Verifica se o método é POST
        form = TarefaForm(request.POST) # Cria o formulário com os dados do POST
        if form.is_valid(): # Verifica se o formulário é válido
            form.save() # Salva a nova tarefa
            return redirect("lista_tarefas") # Redireciona para a lista de tarefas
    else:
        form = TarefaForm() # Cria um formulário vazio para nova tarefa
        return render(request, "form.html", {"form": form}) # Renderiza o formulário para nova tarefa

def editar_tarefa(request, id): # Editar tarefa
    tarefa = get_object_or_404(Tarefa, pk=id) # Busca a tarefa pelo ID
    form = TarefaForm(request.POST or None, instance=tarefa) # Cria o formulário com os dados da tarefa
    if form.is_valid(): # Verifica se o formulário é válido
        form.save() # Salva as alterações na tarefa
        return redirect("lista_tarefas") # Redireciona para a lista de tarefas
    return render(request, "form.html", {"form": form}) # Renderiza o formulário para editar tarefa

def deletar_tarefa(request, id): # Deletar tarefa
    tarefa = get_object_or_404(Tarefa, pk=id) # Busca a tarefa pelo ID
    if request.method == "POST": # Verifica se o método é POST
        tarefa.delete() # Deleta a tarefa
        return redirect("lista_tarefas") # Redireciona para a lista de tarefas
    return render(request, "form.html", {"tarefa": tarefa}) # Renderiza a página de confirmação de deleção