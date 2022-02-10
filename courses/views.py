from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .mixins import ObjectList, ObjectDetail
from .serializers import *


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'courses': reverse('course_list', request=request, format=format),
        'contacts': reverse('contact_list', request=request, format=format),
        'branches': reverse('branch_list', request=request, format=format),
        'categories': reverse('category_list', request=request, format=format)
    })


class CourseList(ObjectList, APIView):
    model = Course
    serializer_class = CourseSerializer
    class_serializer = CourseSerializer


class CourseDetail(ObjectDetail, APIView):
    model = Course
    serializer_class = CourseSerializer
    class_serializer = CourseSerializer


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


class CategoryDetail(ObjectList, APIView):
    model = Category
    class_serializer = CategorySerializer
    serializer_class = CategorySerializer
