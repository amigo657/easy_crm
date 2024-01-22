from django.db import models

class History(models.Model):
    name = models.CharField(max_length=50)
    discription = models.CharField(max_length=50)
    information = models.TextField(max_length=1000)
    coast = models.CharField(max_length=50)
    client_first_name = models.CharField(max_length=50)
    client_last_name = models.CharField(max_length=50)
    client_phone = models.CharField(max_length=50)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=50)
    user_otdel = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"