from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Course, Category, Branch, Contact


class CourseTests(APITestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='test_category_name',
                                           imgpath=None)
        contact = Contact.objects.create(type=1,
                                         value='test_number')
        branch = Branch.objects.create(latitude='test_latitude',
                                       longitude='test_latitude',
                                       address='test_address')
        self.course = Course.objects.create(name='test_course_name',
                                            description='test_course_description',
                                            category=category,
                                            logo=None)
        self.course.save()
        self.course.contacts.add(contact)
        self.course.branches.add(branch)
        self.data = {
            'name': 'test_course_name',
            'description': 'test_course_description',
            'category': category.pk,
            'contacts': contact.pk,
            'branches': branch.pk,
        }

    def test_course_list(self):
        response = self.client.get(reverse('courses:course_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_detail(self):
        response = self.client.get(reverse('courses:course_detail', kwargs={'pk': self.course.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('name'), 'test_course_name')

    def test_fail_course_detail(self):
        response = self.client.get(reverse('courses:course_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_course_create(self):
        response = self.client.post(reverse('courses:course_list'), self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_fail_create(self):
        response = self.client.post(reverse('courses:course_list'), {'': ''}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_course_delete(self):
        response = self.client.delete(reverse('courses:course_detail', kwargs={'pk': self.course.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_course_fail_delete(self):
        response = self.client.delete(reverse('courses:course_detail', kwargs={'pk': 1000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
