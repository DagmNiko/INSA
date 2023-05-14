from rest_framework import serializers
from core.models import Blog
from accounts.models import Account

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ('email', 'password')