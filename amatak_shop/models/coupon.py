"""
Amatak Online Shop
Copyright© Amatak Holdings Pty Ltd licensed under the MIT Agreement.
If you interesting to be part of this project pleaese contact:
Rony MAN <amatak.io@outlook.com>
for business <www.amatak.io>
OpenSource <www.amatak.org>
"""
from django.db import models

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code