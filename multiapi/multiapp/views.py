from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from .models import ImageProduct
from rest_framework import serializers
from .serializers import ProductImageSerializer
from rest_framework import status
from rest_framework import viewsets

class ImageViewSet(viewsets.ViewSet):
    def list(self,request):
        ob=ImageProduct.objects.all()
        serializer=ProductImageSerializer(ob,many=True)
        
            
        return Response(serializer.data)  

    def retrieve(self,request,pk=None):
        if id is not None:
            id=pk
            ob=ImageProduct.objects.get(id=id)
            serializer=ProductImageSerializer(ob)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
    def create(self,request):
        serializer=ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data is created"},status=201)
        return Response(serializer.errors,status=401)
    