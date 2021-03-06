from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .mixins import ObjectList, ObjectDetail
from .serializers import *


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'courses': reverse('courses:course_list', request=request, format=format),
        'contacts': reverse('courses:contact_list', request=request, format=format),
        'branches': reverse('courses:branch_list', request=request, format=format),
        'categories': reverse('courses:category_list', request=request, format=format)
    })


class CourseList(ObjectList, APIView):
    model = Course
    serializer_class = CourseSerializer
    class_serializer = CourseDetailSerializer

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(ObjectDetail, APIView):
    model = Course
    serializer_class = CourseDetailSerializer
    class_serializer = CourseDetailSerializer


class ContactList(ObjectList, APIView):
    model = Contact
    class_serializer = ContactSerializer
    serializer_class = ContactSerializer


class ContactDetail(ObjectDetail, APIView):
    model = Contact
    class_serializer = ContactSerializer
    serializer_class = ContactSerializer


class BranchList(ObjectList, APIView):
    model = Branch
    class_serializer = BranchSerializer
    serializer_class = BranchSerializer


class BranchDetail(ObjectDetail, APIView):
    model = Branch
    class_serializer = BranchSerializer
    serializer_class = BranchSerializer


class CategoryList(ObjectList, APIView):
    model = Category
    class_serializer = CategorySerializer
    serializer_class = CategorySerializer


class CategoryDetail(ObjectDetail, APIView):
    model = Category
    class_serializer = CategorySerializer
    serializer_class = CategorySerializer
