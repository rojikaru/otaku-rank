from rest_framework import serializers

from .genre import Genre
from .demographic import Demographic
from .title import Anime, Manga
from .review import AnimeReview, MangaReview
from .user import User


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""
    def to_internal_value(self, data):
        return data
    def to_representation(self, value):
        return value


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class DemographicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographic
        fields = '__all__'


class AnimeSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    demographics = DemographicSerializer(many=True)
    title_synonyms = JSONSerializerField()
    producers = JSONSerializerField()
    images = JSONSerializerField()

    class Meta:
        model = Anime
        fields = '__all__'

class MangaSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    demographics = DemographicSerializer(many=True)
    title_synonyms = JSONSerializerField()
    producers = JSONSerializerField()
    images = JSONSerializerField()

    class Meta:
        model = Manga
        fields = '__all__'


class AnimeReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimeReview
        fields = '__all__'


class MangaReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangaReview
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            '_id',
            'username',
            'email',
            'password',
            'image',
            'bio',
            'birth_date',
            'created_at',
            'updated_at'
        ]

