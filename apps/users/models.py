from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from apps.users.managers import CustomUserManager


# 1. способ
# class CustomUser(AbstractBaseUser):
#     """Кастомная модель для пользователя"""
#     age = models.PositiveSmallIntegerField()


# 2 способ (РАСПРОСТРАНЕННЫЙ СПОСОБ) *рекомендуется
class CustomUser(AbstractUser):
    """Кастомная модель для пользователя"""
    username = None
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    age = models.PositiveSmallIntegerField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()  # кастомный мененджер модели

    def __str__(self):
        return self.email


# 3 способ
# class CustomUser(models.Model):
#     age = models.PositiveSmallIntegerField()
#     user = models.OneToOneField(to=User, on_delete=models.CASCADE)
