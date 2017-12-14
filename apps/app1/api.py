# -*- coding: utf-8 -*-
import logging

from rest_framework import viewsets

from app1.models import A
from app1.serializers import ASerializer

logger = logging.getLogger(__name__)


class AViewSet1(viewsets.ModelViewSet):

    model = A
    serializer_class = ASerializer
    queryset = A.objects.all()
