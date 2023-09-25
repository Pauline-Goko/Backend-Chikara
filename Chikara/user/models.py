from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    phone_number = PhoneNumberField(unique=True)
    image = models.ImageField(upload_to='user_images/', default="")
    location = models.CharField(max_length=32)
    company_id = models.PositiveIntegerField(default=1)
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(timezone.now(), null=True)
    date_updated = models.DateTimeField(timezone.now(), null=True)

    def __str__(self):
        return self.username


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account', null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        account, created = Account.objects.get_or_create(user=self)
        account.save()
