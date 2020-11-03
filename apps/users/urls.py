
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, UserProfileView

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='user-profile'),
]