from django.test import TestCase

from ..models import Course, Category, Contact, Branch


# Create your tests here.

class CourseModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category = Category.objects.create(name='test_category_name',
                                            imgpath=None)
        contact = Contact.objects.create(type=1,
                                        value='test_number')
        branch = Branch.objects.create(latitude='test_latitude',
                                        longitude='test_latitude',
                                        address='test_address')
        course = Course.objects.create(name='test_course_name',
                              description='test_course_description',
                              category=category,
                              logo=None)
        course.save()
        course.contacts.add(contact)
        course.branches.add(branch)
        cls.course = Course.objects.get(id=1)

    def test_name_label(self):

        field_label = self.course._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):

        field_label = self.course._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_category_label(self):
        field_label = self.course._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

    def test_logo_label(self):
        field_label = self.course._meta.get_field('logo').verbose_name
        self.assertEquals(field_label, 'logo')

    def test_str_def(self):
        self.assertEquals(self.course.__str__(), self.course.name)

    def test_course_name(self):
        self.assertEquals(self.course.name, 'test_course_name')