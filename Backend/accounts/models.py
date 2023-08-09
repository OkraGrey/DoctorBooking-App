from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.


class CustomUserManager(BaseUserManager):

    use_in_migrations=True

    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email is a required field")
        
        if not password:
            raise ValueError("Password is a required field")
        
        extra_fields.setdefault('is_active', False)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        return self.create_user(email, password, **extra_fields)

    def get_by_natural_key(self, email):
        return self.get(email=email)

class CustomUser(AbstractBaseUser):

    objects=CustomUserManager()

    # boolean fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    #choices
    gender_options=(
        ("male","Male"),
        ('female',"Female"),
        ("other","Other"),
    )

    # user
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    date_of_birth = models.DateField(null=True)
    gender=models.CharField(max_length=10,choices=gender_options,default="other")

    #user_name
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['password']

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"    
        return ''

    # Required methods for PermissionsMixin
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True