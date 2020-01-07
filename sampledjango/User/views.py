# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.http import JsonResponse
from django.views.generic.base import View

user_log = logging.getLogger('user')
general_log = logging.getLogger('general')


# Create your views here.
def UserBalance(request):
    if request.method == "GET":
        return JsonResponse({'code': 200, 'msg': 'Your Balance Amount is: 2,00,000 Rs/-'})


class UserProfile(View):

    def get(self, request, *args, **kwargs):
        user_log.info("This is a user log")
        general_log.info("This is a general log")
        return JsonResponse({'code': 200, 'msg': 'Hello, User!'})
