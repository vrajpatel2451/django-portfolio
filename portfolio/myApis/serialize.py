from unicodedata import category
from rest_framework import serializers
from blogs.models import Category, BlogModel,Person,Book

class CategoriesSerilizer(serializers.ModelSerializer):
    blogs = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ('name','blogs')
    def get_blogs(self,cat):
        personModel = BlogModel.objects.filter(category=cat['id'])
        serialized = BlogRecSerilizer(data=personModel.values(),many=True)
        serialized.is_valid(raise_exception=False)
        serialized.save()
        print(serialized.errors)
        return  serialized.data

class CategoriesRecSerilizer(serializers.ModelSerializer):
    # blogs = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
class BookSerializer(serializers.ModelSerializer):
    person = serializers.SerializerMethodField()
    # person_obj = PersonSerializer(source='person',read_only=True)
    class Meta:
        model = Book
        fields = ('title','person')
    def get_person(self,person):
        personModel = Person.objects.filter(id=person['person_id'])
        serialized = PersonSerializer(data=personModel.values(),many=True)
        serialized.is_valid(raise_exception=False)
        serialized.save()
        print(serialized.errors)
        return  serialized.data

class BlogSerilizer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    
    # category_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # category_id = serializers.RelatedField(read_only=True)
    # category_id = CategoriesSerilizer(many=True)
    class Meta:
        model = BlogModel
        fields = ['title','description','category']
    def get_category(self,person):
        personModel = Category.objects.filter(id=person['category_id'])
        serialized = CategoriesRecSerilizer(data=personModel.values(),many=True)
        serialized.is_valid(raise_exception=False)
        serialized.save()
        print(serialized.errors)
        return  serialized.data

class BlogRecSerilizer(serializers.ModelSerializer):
    
    # category_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # category_id = serializers.RelatedField(read_only=True)
    # category_id = CategoriesSerilizer(many=True)
    class Meta:
        model = BlogModel
        fields = ['title','description',]