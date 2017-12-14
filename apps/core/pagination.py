# -*- coding: utf-8 -*-
from rest_framework import pagination


class CustomLimitOffsetPagination(pagination.LimitOffsetPagination):

    def get_paginated_response(self, data):
        response = pagination.LimitOffsetPagination.get_paginated_response(self, data)
        response.data['total'] = response.data['count']
        return response
