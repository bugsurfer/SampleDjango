# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.generic.base import View


# Create your views here.
def UserBalance(request):
    if request.method == "GET":
        return JsonResponse({'code': 200, 'msg': 'Your Balance Amount is: 2,00,000 Rs/-'})


class UserProfile(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse({'code': 200, 'msg': 'Hello, User!'})

