from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *


class ContactSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'type', 'value']


class ContactListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'type', 'value']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'imgpath']


class BranchSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'latitude', 'longitude', 'address']


class BranchListDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'latitude', 'longitude', 'address']


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    contacts = ContactSerializer(many=True, queryset=Contact.objects.all())
    branches = BranchSerializer(many=True, queryset=Branch.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category',
                  'logo', 'contacts', 'branches']
