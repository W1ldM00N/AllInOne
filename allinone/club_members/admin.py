from django.contrib import admin
from .models import ExecutiveCore, Department, User
from django.contrib.auth.admin import UserAdmin
from .models import Membership

# Register your models here.
@admin.register(ExecutiveCore)
class ExecutiveCoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'core')
    list_filter = ('core',)
    search_fields = ('name',)

class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 1

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User

    inlines = [MembershipInline]

    fieldsets = UserAdmin.fieldsets + (
        ("Роль", {
            "fields": ("role",),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Роль", {
            "fields": ("role",),
        }),
    )

    list_display = ('username', 'email', 'role')
    list_filter = ('role', 'department__core', 'department')
    search_fields = ('username', 'email', 'role', 'department')