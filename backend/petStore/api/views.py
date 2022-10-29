#from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.forms.models import model_to_dict

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    data = {"title" : "asd"}
    return Response(data)