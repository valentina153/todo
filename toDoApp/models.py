from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class todo(models.Model):
    naslov = models.CharField(max_length = 100)
    opis = models.TextField(blank = True)
    važno = models.BooleanField(default = False)
    datumZavrsetka = models.DateTimeField(null = True, blank = True)
    userID = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.naslov

