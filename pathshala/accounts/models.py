from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, name, mobile, password=None):
        if not email:
            raise ValueError('User must have an email address')
        if not username:
            raise ValueError('User must have a username')
        if not name:
            raise ValueError('User must have a name')
        if not mobile:
            raise ValueError('User must have a mobile')

        user = Account(
            email=self.normalize_email(email),
            username=username,
            name=name,
            mobile=mobile,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, name, mobile):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            name=name,
            mobile=mobile,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    mobile = models.CharField(blank=True, null=True, max_length=10)
    Class = models.CharField(max_length=20, choices=(("8","8"),("9","9"),("10","10"),("11","11"),("12","12")),default='8')
    Board = models.CharField(max_length=20, choices=(('CBSE', 'CBSE'), ('ICSE', 'ICSE'), ('Other', 'Other')), default='CBSE')
    name = models.CharField(max_length=30)
    selfie = models.ImageField(null=True,upload_to='images')
    Course = models.CharField(max_length=20, choices=(("Regular", "Regular"), ("Crash", "Crash")), default="Regular")
    Mentorship = models.CharField(max_length=20, choices=(("1v1", "1v1"), ("1v5", "1v5")), default="1v1")
    Payment = models.BooleanField(default=False)
    first = models.BooleanField(default=False)
    reg_date = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'mobile', 'name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
