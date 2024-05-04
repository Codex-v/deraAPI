from rest_framework import generics
from .models import DDeatils
from .serializers import DDeatilsSerializer
from rest_framework.response import Response


class DDeatilsListCreate(generics.ListCreateAPIView):
    queryset = DDeatils.objects.all()
    serializer_class = DDeatilsSerializer
    
