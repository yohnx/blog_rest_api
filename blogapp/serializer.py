from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        password = validated_data["password"]
        user = get_user_model()
        new_user = user.objects.create_user(username=username, email=email, 
                                        first_name=first_name,
                                        last_name=last_name, password=password)
        new_user.save()
        return new_user  

class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name", "last_name", "bio", "profile_picture",
                   "youtube", "instagram", "facebook", "twitter"]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"] 

class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'content', 'author', 'created_date', 
                  'updated_date', 'is_draft', 'published_date', 'category', 'featured_image']      
