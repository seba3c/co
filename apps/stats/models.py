# -*- coding: utf-8 -*-
import logging

from django.db import models


logger = logging.getLogger(__name__)


# class A(models.Model):
# 
#     a = models.CharField(max_length=20, null=False, blank=False)
#     b = models.IntegerField(null=False, blank=False)
#     c = models.IntegerField()
# 
#     class Meta:
#         verbose_name = "A"
#         verbose_name_plural = "As"
#         ordering = ['id']
