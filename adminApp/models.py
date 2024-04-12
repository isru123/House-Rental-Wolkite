from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group,Permission
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.urls import reverse
# Create your models here.


class Country(models.Model):
    """Country Model."""

    name = models.CharField(max_length=150, null=False, blank=False, unique=True, default='Ethiopia')
    shortcut = models.CharField(max_length=3, null=False, blank=False, verbose_name="ISO 3166-α2", default='ET')

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        return self.name


class State(models.Model):
    """State Model."""

    country = models.ForeignKey(Country, null=False, on_delete=models.CASCADE, verbose_name=_("Country"))
    name = models.CharField(max_length=150, blank=False, null=False, verbose_name=_("State"))
    shortcut = models.CharField(max_length=6, null=False, blank=False, verbose_name="ISO 3166-2", default='WK')

    class Meta:
        unique_together = ('country', 'shortcut')
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        return f"{self.name} - {self.country.name}"

    def clean(self):
        if self.country.name != 'Ethiopia':
            raise ValidationError("Only Ethiopia is supported as the country.")
        if self.name != 'Wolkite':
            raise ValidationError("Only Wolkite is supported as the state within Ethiopia.")


class Address(models.Model):
    """Address Model."""
    street = models.CharField(max_length=150, blank=False, null=False, verbose_name=_("Street"))
    hn = models.CharField(max_length=15, blank=False, null=False, verbose_name=_("House number"))
    zipcode = models.CharField(max_length=5, blank=False, null=False, verbose_name=_("Zipcode"))
    city = models.CharField(max_length=100, blank=False, null=False, verbose_name=_("City"), default='Wolkite')
    state = models.ForeignKey(State, blank=False, null=False, on_delete=models.CASCADE, verbose_name=_("State"))

    class Meta:
        unique_together = ('street', 'hn', 'zipcode')
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return f"{self.street} {self.hn}, {self.city} - {self.state.country.shortcut}"

    def get_listings(self):
        return self.street

    def clean(self):
        if self.city != 'Wolkite':
            raise ValidationError("Only Wolkite is supported as the city.")
        if self.state.country.name != 'Ethiopia':
            raise ValidationError("Only Ethiopia is supported as the country.")
        


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


    
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, null=True,
                                  verbose_name=_("Firstname"))
    last_name = models.CharField(max_length=255, null=True,
                                 verbose_name=_("Lastname"))
    username = None
    phone = models.CharField(max_length=20, null=True,
                             verbose_name=_("Phone"))
    address = models.CharField(max_length=255, null=True,
                                verbose_name=_("Address"))
    email = models.EmailField(unique=True, verbose_name=_("Email"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    groups  = models.ManyToManyField(
        Group,
        verbose_name='Groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_users'  # Provide a custom related name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='User Permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_users'  # Provide a custom related name
    )
    
    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def get_groups(self):
        return [group.name for group in self.groups.all()]
    get_groups.short_description = _("Groups")


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='realtors/profile/',
                              verbose_name=_("Photo"))
    description = models.TextField(blank=True,
                                   verbose_name=_("Description"))
    phone = models.CharField(max_length=20, verbose_name=_("Phone"))
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(null=True,
                                 verbose_name=_("Hire date"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Realtor")
        verbose_name_plural = _("Realtors")

