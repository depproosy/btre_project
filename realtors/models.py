from django.db import models

class Realtor(models.Model):
  name = models.CharField( max_length=200)
