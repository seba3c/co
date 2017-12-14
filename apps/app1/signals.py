# -*- coding: utf-8 -*-
import logging

from django.db.models.signals import pre_save
from django.dispatch import receiver

from app1.models import A

logger = logging.getLogger(__name__)


@receiver(pre_save, sender=A)
def label_pre_save_signal(sender, instance, **kwargs):
    # do something before save
    pass
