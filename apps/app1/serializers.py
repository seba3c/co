# -*- coding: utf-8 -*-
from rest_framework import serializers

from app1.models import A


class ASerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = 1
        fields = ('id',
                  'a',
                  'b',
                  'c')
        read_only_fields = ('id',)

