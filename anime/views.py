from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from .filter import AnimeFilter
from .models import Anime, Comment
from .pagination import LargeResultsSetPagination
from .serializers import AnimeSerializer, CommentSerializer



class AnimeListAPIView(generics.ListAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, ]
    filterset_fields = ['type', 'year', 'genres']
    filterset_class = AnimeFilter
    search_fields = ['name', ]
    pagination_class = LargeResultsSetPagination




class AnimeDetailAPIView(generics.RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        anime_id = self.kwargs.get('pk')
        anime = get_object_or_404(Anime, id=anime_id)
        serializer.save(anime=anime, user=self.request.user)


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
