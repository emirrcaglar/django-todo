from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Item

def TodoAppView(request):
    all_items = Item.objects.all()
    print(all_items)
    return render(request, 'todolist.html', {'all_items': all_items, 'ACTION_URL': '/todo/'})

def AddTodo(request):
    new_item = Item(content=request.POST['content'])
    if request.POST['content'].strip() != '':
        new_item.save()
    return HttpResponseRedirect('/')

# Delete Todo:
def DeleteTodo(request, pk):
    item = get_object_or_404(Item, id=pk)
    item.delete()
    return redirect('todolist')

# Edit Todo:
def EditTodo(request, pk):
    all_items = Item.objects.all()
    item_to_edit = get_object_or_404(Item, id=pk)
    return render(request, 'edit.html', {'edit_item': item_to_edit, 'all_items': all_items})

# Update Todo Item:
def UpdateTodoItem(request, pk):
    item_to_update = get_object_or_404(Item, id=pk)
    item_to_update.content = request.POST['content']
    item_to_update.save()
    return redirect('todolist')
