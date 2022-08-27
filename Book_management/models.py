from django.db import models

# Create your models here.

class Book(models.Model):
    name =models.CharField(max_length=255)
    ISBN = models.BigIntegerField(unique=True)


    def __str__(self):
        return self.name

    