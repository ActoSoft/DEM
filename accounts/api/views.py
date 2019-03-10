from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer
from ..models import Group, Profile

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer