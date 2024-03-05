from django_filters import rest_framework as filters

from anime.models import Anime

class AnimeFilter(filters.FilterSet):
    year = filters.RangeFilter()

    class Meta:
        model = Anime
        fields = ['type', 'year', 'genres']
