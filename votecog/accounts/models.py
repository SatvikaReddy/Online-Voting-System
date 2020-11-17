from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
from django.utils import timezone

YEAR_CHOICES = (
    ('1st', '1ST'),
    ('2nd','2ND'),
    ('3rd','3RD'),
    ('4th','4TH')
)
DEPT_CHOICES= (
    ('it', 'IT'),
    ('cse', 'CSE'),
    ('civil', 'CIVIL'),
    ('eee', 'EEE'),
    ('ece','ECE'),
    ('chemical','CHEMICAL'),
    ('biotech','BIOTECH'),
    ('mech','MECH'),
    ('prod','PROD'),
)

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username ,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, is_voter, password, email):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_voter = False
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_voter = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    voted = models.CharField(max_length=30, default="no")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','is_voter']

    objects = MyAccountManager()

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Person(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    name = models.CharField(max_length=130)
    branch = models.CharField(max_length=8, choices=DEPT_CHOICES, default='cse')
    year = models.CharField(max_length=6, choices=YEAR_CHOICES, default='1st')
    bio = models.TextField(blank=True)
    status= models.CharField(max_length=130,default="pending")
    published_date = models.DateTimeField(default=timezone.now)
    vote=models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('success')
    
