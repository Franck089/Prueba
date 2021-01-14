from django.db import models


class Cervecera(models.Model):
    cerveceraname = models.CharField(max_length=50)
