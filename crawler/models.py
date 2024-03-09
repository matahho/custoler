from django.db import models

# Create your models here.


class Session(models.Model):
    username = models.CharField(max_length=512)
