from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email addrese')
        if not username:
            raise ValueError('User must have an username')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password=password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    RESTURAUNT = 1
    CUSTOMER = 2
    ROLL_CHOICES = (
        (RESTURAUNT, 'resturaunt'),
        (CUSTOMER, 'customer'),
    )

    first_name = models.CharField(verbose_name='first name', max_length=50)
    last_name = models.CharField(verbose_name='last name', max_length=50)
    username = models.CharField(verbose_name='username', max_length=50, unique=True)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    phone_number = models.CharField(verbose_name='phone number', max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLL_CHOICES, blank=True, null=True)

    # Required fields
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' , 'first_name', 'last_name' ]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True