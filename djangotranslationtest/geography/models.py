# -*- coding: utf-8 -*-
from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255, verbose_name=u'rua')

    class Meta:
        verbose_name = u'endereço'
