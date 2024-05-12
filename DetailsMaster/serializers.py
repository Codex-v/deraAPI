import base64
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from rest_framework import serializers
from .models import DDeatils
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import uuid
import os
from django.core.files.base import ContentFile

class DDeatilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DDeatils
        fields = '__all__'

    def create(self, validated_data):
        # Extract base64 image data from validated_data
        familyDetailContents = validated_data['d_familydeatils']

        # lenthOfContent = len(familyDetailContents)-1
        i = 0
        if familyDetailContents is not None:
            for  familyDetailContent in familyDetailContents:
                imageData = familyDetailContent["image_data"]
                data,base64Data = imageData.split(';')
                name,extension = data.split(":")
                name,base64Value = base64Data.split(":")
                decoded_file = base64.b64decode(base64Value)
                Image = ContentFile(decoded_file)
                
                imageId = str(uuid.uuid4()).replace('-','')
                
                imageName = f"{imageId}.{extension}"
                
                ImagePath = os.path.join(settings.MEDIA_ROOT,imageName)
                
                with open(ImagePath,'wb') as img:
                    img.write(decoded_file)
                
                
                ImageFilePath = os.path.join(settings.MEDIA_URL, ImagePath)
                
                
                tempath = ImageFilePath.replace('\\',"/").split("deraAPI")[1]
                FilePathFinal = "http://103.21.160.164"+tempath
                
                print("FinalImagePath",ImageFilePath)
                # for i in range
                
                
                validated_data['d_familydeatils'][i]['image_data']= FilePathFinal
                i  = i +1


        # Call the default create method to save other fields and return the instance
        instance = super(DDeatilsSerializer, self).create(validated_data)

        return instance

    def post(self, request, *args, **kwargs):
        # Create an instance of the serializer with the incoming data
        serializer = self.get_serializer(data=request.data)

        # Check if the data is valid (calls serializer.validate())
        if serializer.is_valid():
            # If valid, call custom create method to save the instance
            self.perform_create(serializer)
            # Return a response with the created data and a 201 status code
            return Response({"message": "created"}, status=status.HTTP_201_CREATED)
        else:
            # If the data is not valid, return a 400 response with the error details
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
