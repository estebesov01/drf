from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128)
    imgpath = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)
    address = models.CharField(max_length=128)

    def __str__(self):
        return self.address


CONTACT_CHOICES = [
    (1, 'PHONE'),
    (2, 'FACEBOOK'),
    (3, 'EMAIL'),
]


class Contact(models.Model):
    type = models.IntegerField(choices=CONTACT_CHOICES)
    value = models.CharField(max_length=128)

    def __str__(self):
        return self.value


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    logo = models.ImageField(blank=True)
    contacts = models.ManyToManyField(Contact)
    branches = models.ManyToManyField(Branch)

    def __str__(self):
        return self.name
