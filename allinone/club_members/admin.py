from django.contrib import admin
from .models import ExecutiveCore, Department, User
from django.contrib.auth.admin import UserAdmin

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

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
        ("Роль и департамент", {
            "fields": ("role", "department"),
        })
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Роль и департамент", {
            "fields": ("role", "department"),
        }),
    )

    list_display = ('username', 'email', 'role', 'department')
    list_filter = ('role', 'department__core', 'department')
    search_fields = ('username', 'email', 'role', 'department')