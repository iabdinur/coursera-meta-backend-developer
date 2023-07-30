from django.db import models

class Category(models.Model):
    sloug = models.SlugField()
    title = models.CharField(max_length=255)

class MenuItem(models.Model):
    title = models.SlugField()
    price = models.CharField(max_length=255)
    inventory = models.SmallIntegerField(max_digits=6, decimal_place=2)
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
