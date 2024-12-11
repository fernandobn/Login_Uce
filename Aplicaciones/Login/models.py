from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=100, unique=True) 
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user