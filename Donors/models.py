from django.utils import timezone
from django.db import models

class Donor(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    name = models.CharField(max_length=100)
    desig = models.CharField(max_length=30)
    mobile_number = models.CharField(max_length=15)
    bcs_batch = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    last_blood_donation = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.blood_group}"
