from django.urls import path

from apps.genres import views

urlpatterns = [
    path('', views.GenreView.as_view()),
    path('<int:pk>/', views.GenreView.as_view()),
]