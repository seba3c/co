# -*- coding: utf-8 -*-
import logging

from django.utils.translation import ugettext_lazy as _

from django.http.response import Http404

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from django.db.models.deletion import ProtectedError
from django.db.utils import IntegrityError


logger = logging.getLogger(__name__)


class ValidationWarning(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('Warning.')
    default_code = 'warning'


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if isinstance(exc, Http404):
        detail = _('Entidad no encontrada')
        if hasattr(exc, 'message'):
            detail = exc.message
        custom_response_data = {
            'detail': detail  # custom exception message
        }
        response.data = custom_response_data  # set the custom response data on response object

    if isinstance(exc, ProtectedError):
        custom_response_data = {
            'detail': _(u"Error al eliminar: existen relaciones con otras entidades.")
        }
        response = Response(status=status.HTTP_400_BAD_REQUEST)
        response.data = custom_response_data

    if isinstance(exc, IntegrityError):
        custom_response_data = {
            'detail': _(u"No se puede guardar la entidad.")
        }
        response = Response(status=status.HTTP_400_BAD_REQUEST)
        response.data = custom_response_data

    if isinstance(exc, ValidationWarning):
        custom_response_data = {
            'detail': exc.detail,
            'code': exc.default_code
        }
        response.data = custom_response_data

    return response
