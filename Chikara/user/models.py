from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    phone_number = PhoneNumberField(help_text='Contact phone number')
    company_id = models.PositiveIntegerField(default=1)
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(timezone.now(), null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups')
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='user_set', blank=True, help_text='Specific permissions for this user.',
        verbose_name='user permissions')
