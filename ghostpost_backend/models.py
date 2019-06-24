from django.db import models

class BoastsAndRoasts(models.Model):
    boasts = models.CharField(max_length=1000)
    roasts = models.CharField(max_length=1000)
    vote = models.BooleanField(default=False)