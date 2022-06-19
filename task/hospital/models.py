import uuid
from django.db import models
from django.contrib.auth.models import User


USER_TYPES = (
    ('PAT', 'Patient'),
    ('DOC', 'Doctor'),
)

CATAGORIES = (
    ('Mental Health', 'Mental Health'),
    ('Hearth Disease', 'Hearth Disease'),
    ('Covid-19', 'Covid-19'),
    ('Immunization', 'Immunization'),
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

    def __str__(self):
        return str(self.user.username)


class blog(models.Model):
    owner = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    featured_image = models.ImageField(
        null=True, blank=True)
    category = models.CharField(
        max_length=200, choices=CATAGORIES, blank=False, null=False)
    summary = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    is_draft = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.owner)
