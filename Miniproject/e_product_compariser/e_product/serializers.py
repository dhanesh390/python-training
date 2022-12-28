from datetime import datetime

from rest_framework import serializers
from .models import User
from .myconstants import constants


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['user_id', 'user_name', 'contact_number', 'email_id', 'password']


# class UserSerializer(serializers.Serializer):
#     user_id = serializers.CharField(max_length=10)
#     user_name = serializers.CharField(max_length=100)
#     contact_number = serializers.CharField(max_length=10)
#     email_id = serializers.EmailField(max_length=100)
#     password = serializers.CharField(max_length=20)
#     is_active_user = True
#     created_on = datetime.utcnow().strftime(constants.DATE_TIME_FORMAT)
#     updated_on = datetime.utcnow().strftime(constants.DATE_TIME_FORMAT)
#
#     def create(self, validated_data):
#         return User.objects.create(validated_data)
#
#     def update(self, instance, validated_data):
#         instance.user_name = validated_data.get('user_name', instance.user_name)
#         instance.contact_number = validated_data.get('contact_number', instance.contact_number)
#         instance.email_id = validated_data.get('email_id', instance.email_id)
#         instance.password = validated_data.get('password', instance.password)
#         instance.created_on = validated_data.get('created_on', instance.created_on)
#         instance.updated_on = validated_data.get('updated_on', instance.updated_on)

