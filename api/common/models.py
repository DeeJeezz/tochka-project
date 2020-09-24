from django.db import models
import uuid


class Account(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fio = models.CharField(max_length=150)
    balance = models.IntegerField()
    hold = models.IntegerField()
    status = models.BooleanField(default=True)
