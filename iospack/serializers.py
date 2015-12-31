__author__ = 'gavin'

from django.contrib.auth.models import User, Group
from iospack.models import App
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    apps = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name = 'app-detail')

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups', 'apps')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class AppSerializer(serializers.HyperlinkedModelSerializer):

    owner = UserSerializer(source='owner.username')
    class Meta:
        model = App
        fields = ('id', 'name', 'icon', 'launcher', 'version', 'bundle_id', 'owner')