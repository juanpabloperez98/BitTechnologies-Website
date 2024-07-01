from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from api.models import Property
from api.serializers import PropertySerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cerberus import Validator
from api.helpers import (
    StandardErrorHandler, 
    property_type_allowed
)
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Api Class
class PropertyAPI(APIView):
    
    def get(self, request, pk=None):
        """ Get propertys """
        if pk is not None:
            # Si se proporciona un ID (pk), obtener una propiedad específica por su ID
            property_obj = get_object_or_404(Property, pk=pk)
            serializer = PropertySerializer(property_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Si no se proporciona un ID, listar todas las propiedades
            properties = Property.objects.all()
            serializer = PropertySerializer(properties, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """ Save property"""
        validator = Validator(
            {
                "name": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                },
                "address": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                },
                "country": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                },
                "city": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                },
                "postal_code": {
                    "type": "string",
                    "required": True,
                    "regex": "^\d+$",  # Asegura que postal_code sea numérico
                },
                "property_type": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                    "allowed": property_type_allowed,  # Validar contra los valores permitidos
                },
                "surface": {
                    "type": "string",
                    "required": True,
                },
            }, error_handler=StandardErrorHandler
        )

        if not validator.validate(request.data):
            return Response(
                {"error": "VALIDATION_ERROR", "details": validator.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = PropertySerializer(data=validator.document)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"error": "VALIDATION_ERROR", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk):
        """Update property"""
        validator = Validator(
            {
                "name": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                },
                "address": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                },
                "country": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                },
                "city": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                },
                "postal_code": {
                    "type": "string",
                    "required": True,
                    "regex": "^\d+$",  # Asegura que postal_code sea numérico
                },
                "property_type": {
                    "type": "string",
                    "required": True,
                    "empty": False,
                    "allowed": ["house", "apartment", "office"],  # Validar contra los valores permitidos
                },
                "surface": {
                    "type": "string",
                    "required": True,
                },
            }, error_handler=StandardErrorHandler
        )
        
        if not validator.validate(request.data):
            return Response(
                {"error": "VALIDATION_ERROR", "details": validator.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        try:
            property = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response(
                {"error": "NOT_FOUND", "details": f"Property with id {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
            
        serializer = PropertySerializer(property, data=validator.document, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "VALIDATION_ERROR", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
            
    def delete(self, request, pk):
        """ Delete Property by ID """
        try:
            property_instance = Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Response(
                {"error": "NOT_FOUND", "details": f"Property with id {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        
        property_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)