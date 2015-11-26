from __future__ import unicode_literals

from rest_framework import serializers
from app.core.models import Application

class AppSerializer(serializers.ModelSerializer):
	fields = serializers.StringRelatedField(many=True)
	class Meta:
		model = Application
		fields = ('name', 'slug', 'fields', )