from django.contrib.auth.models import User
from django.db import models

# Create your models here.

TYPE = (
    (1, "fundacja"),
    (2, "organizacja pozarządowa"),
    (3, "Zbiórka lokalna"),
    (4, "domyślnie fundacja")

)

"""Simple Category entry. Instance of this model describes the type of donated objects"""

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

"""Institution model - used to decribe the institution to which the donation is going.
Related to: Category"""

class Institution(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    type = models.IntegerField(choices=TYPE)
    categories = models.ManyToManyField('Category')

"""Donation models saves the total donation with all it's information, ushc as address, pickup yime etc.
Related to: Category, Institution and User"""

class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField('Category')
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=64)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
