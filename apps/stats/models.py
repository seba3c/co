# -*- coding: utf-8 -*-
import logging

from django.db import models


logger = logging.getLogger(__name__)


class IntranetMachine(models.Model):
    ip = models.GenericIPAddressField()
    port = models.IntegerField(null=False, blank=False)


class IntranetMachineStats(models.Model):

    timestamp = models.DateField(auto_now_add=True)
    os_name = models.CharField(max_length=20)
    mem_usage = models.FloatField()
    cpu_usage = models.FloatField()
    total_uptime = models.FloatField()

    intranet_machine = models.ForeignKey(IntranetMachine, on_delete=models.CASCADE,
                                         related_name="stats")


# TODO: model for security events logs in Windows Machines
