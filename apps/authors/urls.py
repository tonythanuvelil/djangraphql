from django.urls import path, include
from .views import AuthorView

urlpatterns = [
    path('', AuthorView.as_view(), name='author'),
]
