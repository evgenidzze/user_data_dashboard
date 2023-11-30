from django.shortcuts import render
from rest_framework import viewsets
from .models import UserActions
from .serializers import UserActionsSerializer


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserActionsSerializer
    queryset = UserActions.objects.all()


def users(request):
    return render(request, 'real_time_users/main.html')
