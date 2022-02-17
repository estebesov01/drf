from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *


class ContactCreateSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'type', 'value']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'imgpath']


class BranchCreateSerializer(PrimaryKeyRelatedField, serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'latitude', 'longitude', 'address']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'latitude', 'longitude', 'address']


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    contacts = ContactCreateSerializer(many=True, queryset=Contact.objects.all())
    branches = BranchCreateSerializer(many=True, queryset=Branch.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'name', 'description',
                  'logo', 'contacts', 'branches', 'category', ]


class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    contacts = ContactSerializer(many=True, read_only=True)
    branches = BranchSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
