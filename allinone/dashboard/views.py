from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from club_members.models import Membership, User


# Create your views here.
class DashboardView(LoginRequiredMixin, TemplateView):
    def get_department(self):
        dept_id = self.request.GET.get("department_id")
        user_depts = self.request.user.department.all()

        if dept_id:
            return user_depts.filter(id=dept_id).first() or user_depts.first()

        return user_depts.first()

    def get_template_names(self):
        department = self.get_department()
        effective_role = self.request.user.effective_role(department)
        dept_slug = department.name.lower() if department else "default"

        return [
            f"dashboard/{dept_slug}/{effective_role}.html",
            f"dashboard/{effective_role}.html",
            f"dashboard/default.html",
        ]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        department = self.get_department()
        ctx["department"] = department
        ctx["core"] = department.core if department else None
        ctx['effective_role'] = self.request.user.effective_role(department)
        ctx['my_departments'] = self.request.user.department.all()

        if self.request.user.role in [User.Role.HEAD, User.Role.FOUNDER, User.Role.SENIOR_MANAGER]:
            primary_membership = Membership.objects.filter(user=self.request.user, is_primary=True).first()
            if primary_membership:
                ctx['core_departments'] = primary_membership.department.core.departments.all()

        return ctx
