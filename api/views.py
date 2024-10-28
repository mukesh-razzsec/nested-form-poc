from rest_framework import generics
from django.shortcuts import render

from api.models import Package
from api.serializers import PackageSerializer


# Create your views here.
class PackageView(generics.CreateAPIView):
    serializer_class = PackageSerializer
    queryset = Package.objects.all()


def create_package_view(request):
    return render(request, "api/index.html")
