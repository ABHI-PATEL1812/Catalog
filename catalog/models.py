from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30, unique=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)


class BookCatalog(models.Model):
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.CharField(max_length=30)
    publish_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    sold_count = models.BigIntegerField()

