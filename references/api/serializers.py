from ..models import *
from rest_framework import serializers

class ReferencesFromSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reference
		fields = ('from_group', 'to_group', 'extras', 'date_created',)

class ReferencesToSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reference
		fields = ('from_group', 'to_group', 'extras', 'date_created')