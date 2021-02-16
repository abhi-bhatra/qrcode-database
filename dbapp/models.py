from django.db import models
from django.db.models.base import Model

# Create your models here.
YEAR_IN_SCHOOL_CHOICES = [
    ('FB', 'Fully_buffed'),
    ('HS', 'Horizontal_satin'),
    ('VS', 'Vertical_satin'),
    ('CS', 'Circular_satin'),
]
class Entry(models.Model):
    Fully_buffed='FB'
    Horizontal_satin='HS'
    Vertical_satin='VS'
    Circular_satin='CS'
    YEAR_IN_SCHOOL_CHOICES = [
        (Fully_buffed, 'Fully buffed'),
        (Horizontal_satin, 'Horizontal satin'),
        (Vertical_satin, 'Vertical satin'),
        (Circular_satin, 'Circular satin'),
    ]

    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=Fully_buffed,
    )
    # idname = models.CharField(max_length=10, null=True)
    # modelname = models.CharField(max_length=300, null=True)

    def __str__(self):
        return (self.year_in_school)

class Cmodel(models.Model):
    title=models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.title)

class Customer(models.Model):
    cname=models.CharField(max_length=30, null=True)
    cnumber=models.CharField(max_length=10, null=True)
    cmodel=models.ForeignKey(Cmodel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return(self.cname+" , "+self.cnumber)