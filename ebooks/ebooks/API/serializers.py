from rest_framework import serializers
from ebook.models import Ebook, Review

# Just a comment


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        models = Review
        fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        models = Ebook
        fields = "__all__"
