# File Path: API-Rock_of_Ages_NSS-Python-Django/rockapi/models/type.py

from django.db import models


class Type(models.Model):
    label = models.CharField(max_length=155)