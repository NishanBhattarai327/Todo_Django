from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoCreateForm

# Create your views here.
def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todos/todo_list.html', {'todos' : todos})

def todo_create(request):
    if request.method == 'POST':
        print('post::::::========================================>>>>')
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoCreateForm()
    return render(request, 'todos/todo_create.html', {'form' : form})

def todo_delete(request, todo_id):
    todo = get_object_or_404(TodoItem, pk=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todos/todo_delete_confirm.html', {'todo' : todo})

