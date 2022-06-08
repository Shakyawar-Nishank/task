from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import User


USER_TYPES = (
    ('PAT', 'Patient'),
    ('DOC', 'Doctor'),
)


class hospital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
        max_length=200, choices=USER_TYPES, blank=False, null=False)
    profile_image = models.ImageField(
        blank=True, null=True)
    address_line_1 = models.CharField(
        max_length=500, blank=False, null=False)
    city = models.CharField(
        max_length=200, blank=False, null=False)
    state = models.CharField(
        max_length=200, blank=False, null=False)
    pincode = models.CharField(max_length=6, blank=False, null=False)
