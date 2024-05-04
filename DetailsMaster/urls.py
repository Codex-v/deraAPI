from django.urls import path
from .views import *

urlpatterns = [
    path("fillDeatils",DDeatilsListCreate.as_view(), name="list details")
]
