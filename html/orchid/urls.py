from django.conf.urls import patterns, include, url
from rest_framework import routers

from orchid import views


router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)
router.register(r'identities', views.IdentityViewSet)

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^photo/(?P<photo_id>\d+)/$', views.photo, name='photo'),
    url(r'^photo/(?P<photo_id>\d+)/identify/$', views.identify, name='identify'),
    url(r'^photo/(?P<photo_id>\d+)/identity/$', views.photo_identity, name='identity'),
    url(r'^photo/(?P<photo_id>\d+)/delete/$', views.delete_photo, name='delete_photo'),
    url(r'^library/$', views.my_photos, name='library'),
    url(r'^session_data\.json$', views.json_get_session_data, name='session_data'),
    url(r'^orchid\.js$', views.javascript, name='js'),

    # API endpoints
    url(r'^api/', include(router.urls, namespace='api')),
)
