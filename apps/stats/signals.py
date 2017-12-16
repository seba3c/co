# -*- coding: utf-8 -*-
import logging

from django.db.models.signals import pre_save
from django.dispatch import receiver

logger = logging.getLogger(__name__)
