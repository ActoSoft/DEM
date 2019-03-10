from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import *
#from ..models import Group, Profile

class ReferencesFromViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Reference.objects.all()
	serializer_class = ReferencesFromSerializer

class ReferencesToViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Reference.objects.all()
	serializer_class = ReferencesToSerializer	