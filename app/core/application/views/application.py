# -*- coding: utf-8 -*-

from rest_framework import viewsets, exceptions, response
from app.api.pagination import CustomPagination
from app.core.application.serializers import AppSerializer, Application

class AppViewSet(viewsets.ModelViewSet):
	model = Application
	serializer_class = AppSerializer

	def get_queryset(self):
		queryset = Application.objects.all()
		loadtype = self.request.query_params.get('loadtype', None)
		if loadtype == 'results':
		    self.pagination_class = CustomPagination

		query = self.request.query_params.get('q', None)

		if query:
			try:
				queryset = [Application.objects.get(slug=query)]
			except Exception, e:
				pass

		return queryset