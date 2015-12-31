# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from iospack.models import App
from rest_framework import viewsets
from rest_framework import generics
from iospack.serializers import UserSerializer, GroupSerializer, AppSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑user 的 API endpoint
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑group的 API endpoint
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AppsViewSet(viewsets.ModelViewSet):
    """
    允许查看和编辑app的 API endpoint
    """
    queryset = App.objects.all()
    serializer_class = AppSerializer
    lookup_field = 'bundle_id'

class app(generics.RetrieveUpdateDestroyAPIView):
    """
    根据app_id获取app信息
    """
    queryset = App.objects.all()
    serializer_class = AppSerializer
    lookup_field = 'id'