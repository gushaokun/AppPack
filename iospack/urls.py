__author__ = 'gavin'
from django.conf.urls import patterns, url, include
from rest_framework import routers
from iospack import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
router.register(r'apps', views.AppsViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
