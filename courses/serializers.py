from rest_framework import serializers

from .models import *


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'type', 'value']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'imgpath']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'latitude', 'longitude', 'address']


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    contacts = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())
    branches = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'category',
                  'logo', 'contacts', 'branches']

    def create(self, validated_data):
        return Course.objects.create(**validated_data)
        # contacts_data = validated_data.pop('contacts')
        # branches_data = validated_data.pop('branches')
        # course = Course.objects.create(**validated_data)
        # print(**validated_data)
        # for contact in contacts_data:
        #     contact, created = Contact.objects.get_or_create(id=contact['id'])
        #     course.contacts.add(contact)
        # for branch in branches_data:
        #     branch, created = Branch.objects.get_or_create(id=branch['id'])
        #     course.branches.add(branch)
        # return course
