from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ExecutiveCore(models.Model):
    name = models.CharField(max_length=50)

class Department(models.Model):
    core = models.ForeignKey(ExecutiveCore, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=50)

class User(AbstractUser):
    class role(models.TextChoices):
        INTERN = "Intern", "Стажер"
        NOVICE = "Novice", "Новичок"
        CONSULTANT = "Consultant", "Консультант"
        SENIOR_CONSULTANT = "Senior consultant", "Старший консультант"
        DEPUTY_MANAGER = "Deputy manager", "Заместитель менеджера"
        MANAGER = "Manager", "Менеджер"
        SENIOR_MANAGER = "Senior manager", "Старший менеджер"
        HEAD = "Head", "Глава направления"
        FOUNDER = "Founder"

    role = models.CharField(max_length=20, choices=role.choices, default=role.INTERN)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)