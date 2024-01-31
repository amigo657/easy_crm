from django.shortcuts import render, redirect
from django.contrib import messages
from .models import History, The_note
from .forms import AddHistoryForm
from website.models import Project

def view_history(request):
    # history = History.objects.all()
    history = Project.objects.filter(status = 'В работе')
    return render(request, "history.html", {"history": history})

def history_item(request, pk):
    history = Project.objects.get(id=pk)
    notes = The_note.objects.filter(project_id=pk).select_related('user')
    steps = [
        ('Планирование', 1),
        ('Моделирование', 2),
        ('Моделирование бд', 3),
        ('Дизайн', 4),
        ('Начало разрабоки', 5),
        ('Разработка', 6),
        ('Тестирование', 7),
        ('Закончен', 8)
    ]
    context = {
        "history": history,
        "notes": notes,
        "steps": steps,  # Исправлено на "steps"
    }
    return render(request, "history_item.html", context)

def change_item(request, pk):
    if request.user.is_authenticated:
        del_history = History.objects.get(id=pk)
        del_history.delete()
        messages.success(request, "Вы удалили запись")
        return redirect("view_history")
    else:
        messages.error(request, "Вы не являетесь админом")
        return redirect("view_history")
    
# def update_item(request, pk):
#     if request.user.is_authenticated:
#         history = History.objects.get(id=pk)
#         form = AddHistoryForm(request.POST or None, instance=history)
#         if form.is_valid():
#             updated_item = form.save()
#             messages.success(request, f"Запись '{updated_item.name}' была обновлена")
#             return redirect("view_history")
#         return render(request, "update_record.html", {"form": form})
#     else:
#         messages.error(request, "You have to login")
#         return redirect("view_history")

# def add_item(request):
#     form = AddHistoryForm(request.POST or None)
#     if request.user.is_authenticated:
#         if form.is_valid():
#             add_history_item = form.save()
#             messages.success(request, f"Запись {add_history_item.name} была добавлена")
#             return redirect("view_history")
#         return render(request, "add_item.html", {"form": form})
#     else:
#         messages.error(request, "You have to login")
#         return redirect("view_history")