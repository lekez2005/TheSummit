from tastypie.resources import ModelResource
from summit_app.models import Content

class ContentResource(ModelResource):
	class Meta:
		queryset = Content.objects.all()
		allowed_methods = ['get']