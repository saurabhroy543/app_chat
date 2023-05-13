from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from .managers import CustomUserManager

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(_('created'), auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(_('modified'), auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.created_by is None:
            self.created_by = self._get_user()
        super().save(*args, **kwargs)

    def _get_user(self):
        from django.contrib.auth import get_user
        print(get_user(self.request))
        return get_user(self.request)


class Interest(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    phone_no = models.CharField(max_length=13, null=True, blank=True,unique=True)
    gender = models.CharField(max_length=5, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    interest = models.ManyToManyField(Interest, related_name='user_interest')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email