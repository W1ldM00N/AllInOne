from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.
class ExecutiveCore(models.Model):
    name = models.CharField(max_length=50)

class Department(models.Model):
    core = models.ForeignKey(ExecutiveCore, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=50)

class Membership(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'department')

class User(AbstractUser):
    class Role(models.TextChoices):
        INTERN = "Intern", "Стажер"
        NOVICE = "Novice", "Новичок"
        CONSULTANT = "Consultant", "Консультант"
        SENIOR_CONSULTANT = "Senior consultant", "Старший консультант"
        DEPUTY_MANAGER = "Deputy manager", "Заместитель менеджера"
        MANAGER = "Manager", "Менеджер"
        SENIOR_MANAGER = "Senior manager", "Старший менеджер"
        HEAD = "Head", "Глава направления"
        FOUNDER = "Founder"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.INTERN)
    department = models.ManyToManyField(Department, through=Membership, related_name='members')

    DOWNGRADE_MAP = {
        Role.SENIOR_MANAGER: Role.DEPUTY_MANAGER,
        Role.HEAD: Role.DEPUTY_MANAGER,
        Role.MANAGER: Role.DEPUTY_MANAGER,
    }

    def effective_role(self, department):
        membership = Membership.objects.filter(user=self, department=department).first()

        if not membership:
            return None

        core_0 = ExecutiveCore.objects.filter(name="Core_0").first()

        if department.core == core_0:
            return self.role

        if membership.is_primary:
            return self.role

        return self.DOWNGRADE_MAP.get(self.role, self.role)
