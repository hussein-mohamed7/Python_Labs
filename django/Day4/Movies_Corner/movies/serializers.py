from rest_framework import serializers
from .models import (
    Movie,
    Series,
    Category,
    Cast
)

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class CastSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cast
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):

    categories = serializers.StringRelatedField(
        many=True
    )

    casts = serializers.StringRelatedField(
        many=True
    )

    class Meta:
        model = Movie
        fields = '__all__'