from django.db import models


class Project(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.IntegerField()
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length = 50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
