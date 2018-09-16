# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Search(APIView):
  def post(self, request):
    query = request.POST.get("query")
    print request.POST
    data = {
      "received_query": query
    }
    return Response(data)