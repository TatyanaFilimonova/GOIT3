from django.db import models
from django.contrib.sessions.models import Session

# Create your models here.


class History(models.Model):
    session = models.ForeignKey(Session,  related_name='session_current', on_delete=models.CASCADE)
    response = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=200, null=False)
    body = models.BinaryField(null=False)
    type = models.CharField(max_length=5, null=False)


class Models(models.Model):
    name = models.CharField(max_length=20, null=False)
    model = models.BinaryField(null=False)

