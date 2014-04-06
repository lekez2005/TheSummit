from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from tastypie.api import Api
from api.resources import ContentResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(ContentResource())
v1_api.register(UserResource())

admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^api/', include(v1_api.urls)),
    url(r'^summit_app/', include('summit_app.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
