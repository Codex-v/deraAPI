from rest_framework import serializers
from .models import *
from rest_framework.response import Response
from rest_framework import status


class DDeatilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DDeatils
        fields = '__all__'

    def post(self, request, *args, **kwargs):
        # Create an instance of the serializer with the incoming data
        serializer = self.get_serializer(data=request.data)
        
        print(request.FIELS)
        
        # Check if the data is valid (calls serializer.validate())
        if serializer.is_valid():
            # If valid, save the instance (calls serializer.create())
            self.perform_create(serializer)
            # Return a response with the created data and a 201 status code
            return Response({"message":"created"}, status=status.HTTP_201_CREATED)
        else:
            # If the data is not valid, return a 400 response with the error details
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)