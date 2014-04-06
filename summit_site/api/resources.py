from django.contrib.auth.models import User
from tastypie.authorization import Authorization
from tastypie import fields
from tastypie.resources import ModelResource
from summit_app.models import Content

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'last_login']

class ContentResource(ModelResource):
	author = fields.ForeignKey(UserResource, 'author')
	class Meta:
		queryset = Content.objects.all()
		authorization = Authorization()
		resource_name = 'content'