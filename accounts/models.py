from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        USER = 'USER', 'User'
        MANAGER = 'MANAGER', 'Manager'

    role = models.CharField(max_length=15, choices=Role.choices, default=Role.USER)


    @property
    def is_admin(self)->bool:
        return self.role == self.Role.ADMIN
    
    @property
    def is_user(self)->bool:
        return self.role == self.Role.USER
    
    @property
    def is_manager(self)->bool:
        return self.role == self.Role.MANAGER