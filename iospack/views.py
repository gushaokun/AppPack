# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
from iospack.models import AppInfo
from rest_framework import viewsets
from iospack.serializers import UserSerializer, GroupSerializer, AppInfoSerializer


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
    queryset = AppInfo.objects.all()
    serializer_class = AppInfoSerializer

    lookup_field = 'bundle_id'
