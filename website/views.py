from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Project


def home(request):
    records = Project.objects.filter(status = 'На рассмотрении')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You've been logged in")
            return redirect("home")
        else:
            messages.warning(request, "A mistake occured, Try one more time")
            return redirect("home")
    else:
        return render(request, "home.html", {"records": records})


def logout_user(request):
    logout(request)
    messages.success(request, "You logged out")
    return redirect("home")


def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Вы зарегестрировались")
            return redirect("home")
        else:
            messages.error(request, "Возникла ошибка. Попробуйте еще раз")

    return render(request, "register.html", {"form": form})


def record(request, pk):
    if request.user.is_authenticated:
        record = Project.objects.get(id=pk)
        return render(request, "record.html", {"record": record})
    else:
        messages.error(request, "Вы вошли в аккаунт")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        del_record = Project.objects.get(id=pk)
        del_record.delete()
        messages.success(request, "Вы удалили запись")
        return redirect("home")
    else:
        messages.error(request, "Вы не являетесь админом")
        return redirect("home")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if form.is_valid():
            add_record = form.save()
            messages.success(request, f"Запись {add_record.first_name} была добавлена")
            return redirect("home")
        return render(request, "add_record.html", {"form": form})
    else:
        messages.error(request, "You have to login")
        return redirect("home")


def update_record(request, pk):
    if request.user.is_authenticated:
        record = Project.objects.get(id=pk)
        record.status = 'В работе'
        record.save() 
        # form = AddRecordForm(request.POST or None, instance=record)
        return redirect("home")
    else:
        pass
    #     if form.is_valid():
    #         updated_record = form.save()
    #         messages.success(request, f"Запись '{updated_record.first_name}' была обновлена")
    #         return redirect("home")
    #     return render(request, "update_record.html", {"form": form})
    # else:
    #     messages.error(request, "You have to login")
    #     return redirect("home")
