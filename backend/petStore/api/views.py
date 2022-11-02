#from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from animals.models import Categories, Status, Tags, Animal, AnimalForm
from api.serializers import AnimalSerializer

from django.http import JsonResponse


# @api_view(['POST'])
# def api_post(request, *args, **kwargs):

#     serializer = AnimalSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         instance = serializer.save() #in case of modification
#         return Response(serializer.data)
#     return Response({"invalid": "Invalid data"}, status=405)

class AnimalDetailAPIView(generics.RetrieveAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

api_pet_detailed_view = AnimalDetailAPIView.as_view()

@api_view(['GET', 'DELETE', 'POST'])
def api_pet_by_id(request, pk=None, *args, **kwargs):
    method = request.method
    print(method)
    print(pk)
    if pk == None:
        return Response(status=405)
    animal = Animal.objects.filter(pk=pk)
    animal = animal.first()
    if method == 'GET': #use pk
        if animal is not None:
            data = AnimalSerializer(animal, many=False).data
            print(data)
            return Response(data, status=200)
        return Response(status=404)
    if method == 'DELETE': #use pk
        if animal is not None:
            data = AnimalSerializer(animal, many=False).data
            animal.delete()
            return Respone(data, status=200)
        return Response(status=404)
    if method == 'POST': # x-www-form-urlencoded
        # serializer = AnimalSerializer(data=request.data)
        form = AnimalForm(request.POST)
        if form.is_valid(raise_exception=True):
            instance = form.save() #in case of modification
            return Response(form.data)
    return Response(status=405)
    return

# @api_view(['GET'])
# def api_get(request, *args, **kwargs):
#     serializer = AnimalSerializer(data=request.data)
#     return Response(status=404)
@api_view(['GET'])
def api_find_by_status(request, *args, **kwargs):
    #print("in find by status")
    params = request.query_params
    #print(params["status"])
    params = set(params["status"].split(','))
    #print(params)
    if params == []:
        params = ['available']
    to_exclude = set(['available', 'pending', 'sold'])
    to_exclude = to_exclude - params
    #print(to_exclude)
    result = Animal.objects.exclude(status__in=to_exclude)
    #print(result)
    data = AnimalSerializer(result, many=True).data
    #print(data)
    return Response(list(data))

@api_view(['POST'])
def api_upload_picture(request, *args, **kwargs):
    return Response(status=405)

@api_view(['POST', 'PUT'])
def api_pet(request, *args, **kwargs):
    method = request.method

    if method == "POST":
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save() #in case of modification
            return Response(serializer.data)
        return Response({"invalid": "Invalid data"}, status=405)
    if method == "PUT":
        data = request.data
        #print("under put method")
        pkey = data.get('id')
        #print(pkey)
        if pkey is not None:
            if not Animal.objects.filter(id=pkey):
                return Response({"Description" : "Pet not found"}, status=404)
            serializer = AnimalSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = serializer.save()
                return Response(status=201)
    return Response(status=405)