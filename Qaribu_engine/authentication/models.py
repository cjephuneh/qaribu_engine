from django.db import models

# Create your models here.

class UserRegister(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class UserLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    




    
    class Meta: 
        db_table = 'user'

    def __str__(self):
        return self.name