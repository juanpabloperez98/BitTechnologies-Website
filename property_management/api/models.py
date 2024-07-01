from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('office', 'Office'),
    ]

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    surface = models.CharField(max_length=10)

    def __str__(self):
        return self.name
