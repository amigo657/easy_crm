from django import forms
from .models import History

class AddHistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "discription": forms.TextInput(attrs={"class": "form-control"}),
            "information": forms.TextInput(attrs={"class": "form-control"}),
            "coast": forms.TextInput(attrs={"class": "form-control"}),
            "client_first_name": forms.TextInput(attrs={"class": "form-control"}),
            "client_last_name": forms.TextInput(attrs={"class": "form-control"}),
            "client_phone": forms.TextInput(attrs={"class": "form-control"}),
            "user_first_name": forms.TextInput(attrs={"class": "form-control"}),
            "user_last_name": forms.TextInput(attrs={"class": "form-control"}),
            "user_phone": forms.TextInput(attrs={"class": "form-control"}),
            "user_otdel": forms.TextInput(attrs={"class": "form-control"}),
        }