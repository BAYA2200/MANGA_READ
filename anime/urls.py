from django.urls import path

from . import views

urlpatterns = [
    path('anime/list/', views.AnimeListAPIView.as_view()),
    path('anime/<int:pk>/', views.AnimeDetailAPIView.as_view()),
    path('anime/<int:pk>/comment/create/', views.CommentCreateAPIView.as_view()),
    path('anime/<int:pk>/comment/list/', views.CommentListAPIView.as_view()),

]