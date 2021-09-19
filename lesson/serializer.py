from rest_framework import serializers
from lesson.models import Book,Chapter


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name','section','grade','study_field','page')


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('name','number')