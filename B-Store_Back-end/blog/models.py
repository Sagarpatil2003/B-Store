from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="Book_pic", blank=True, null=True)
    description = models.TextField()
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if not self.title:
            raise ValidationError("The title field cannot be empty.")

    def __str__(self):
        return self.title
