from django.db import models


class DepositModel(models.Model):
    deposit = models.IntegerField()
    term = models.IntegerField()
    rate = models.FloatField()
    interest = models.FloatField()
