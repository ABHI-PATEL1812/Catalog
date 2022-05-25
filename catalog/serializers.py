from rest_framework import serializers
from .models import Author,Category,BookCatalog


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', )


class BookCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCatalog
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(BookCatalogSerializer, self).to_representation(instance)
        if self.context['request'].method=="GET":
            rep['author'] = instance.author.name
            rep['category'] = instance.category.name
        return rep


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id', )