from django.shortcuts import render, redirect
from django.contrib import messages
from .models import History
from .forms import AddHistoryForm

def view_history(request):
    history = History.objects.all()
    return render(request, "history.html", {"history": history})

def history_item(request, pk):
    history = History.objects.get(id=pk)
    return render(request, "history_item.html", {"history": history})

def delete_item(request, pk):
    if request.user.is_authenticated:
        del_history = History.objects.get(id=pk)
        del_history.delete()
        messages.success(request, "Вы удалили запись")
        return redirect("view_history")
    else:
        messages.error(request, "Вы не являетесь админом")
        return redirect("view_history")
    
def update_item(request, pk):
    if request.user.is_authenticated:
        history = History.objects.get(id=pk)
        form = AddHistoryForm(request.POST or None, instance=history)
        if form.is_valid():
            updated_item = form.save()
            messages.success(request, f"Запись '{updated_item.name}' была обновлена")
            return redirect("view_history")
        return render(request, "update_record.html", {"form": form})
    else:
        messages.error(request, "You have to login")
        return redirect("view_history")

def add_item(request):
    form = AddHistoryForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            add_history_item = form.save()
            messages.success(request, f"Запись {add_history_item.name} была добавлена")
            return redirect("view_history")
        return render(request, "add_item.html", {"form": form})
    else:
        messages.error(request, "You have to login")
        return redirect("view_history")