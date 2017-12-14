# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include

from rest_framework.routers import SimpleRouter

from app1.api import (AViewSet1, )

API_VERSION = 'v1'

API_PREFIX = "api/%s" % API_VERSION

api_router = SimpleRouter()

api_router.register(r'%s/app1-ex1' % API_PREFIX,
                    AViewSet1, base_name='app1-ex1')

urlpatterns = [url(r'^', include(api_router.urls)),
               ]
