from django.db import models
from datetime import datetime

class BoastsAndRoasts(models.Model):
    boasts = models.CharField(blank=True, max_length=1000, default="boast?")
    roasts = models.CharField(blank=True, max_length=1000, default="roast?")
    vote = models.BooleanField(default=False)
    dateCreated = models.DateTimeField(default=datetime.now(), blank=True)