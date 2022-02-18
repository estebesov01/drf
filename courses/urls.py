from django.urls import path
from .views import *

urlpatterns = [
    path('/', api_root),
    path('courses/', CourseList.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course_detail'),
    path('contacts/', ContactList.as_view(), name='contact_list'),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact_detail'),
    path('branches/', BranchList.as_view(), name='branch_list'),
    path('branches/<int:pk>/', BranchDetail.as_view(), name='branch_detail'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
]
