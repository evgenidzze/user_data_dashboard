from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UsersViewSet, basename='users')

urlpatterns = [
    path('', views.users)
]

urlpatterns += router.urls
