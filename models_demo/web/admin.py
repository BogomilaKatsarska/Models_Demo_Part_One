from django.contrib import admin

from models_demo.web.models import Employee, NullBlankDemo, Department, Project, Category


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name')
    list_filter = ('level', 'department_id')
    search_fields = ('first_name', 'last_name')
    sortable_by = ('id', 'first_name', 'last_name')

    fieldsets = (
        (
            'Personal Info',
            {
             'fields': ('first_name', 'last_name', 'age'),
            }
        ),
        (
            'Professional Info',
            {
                'fields': ('level', 'years_of_experience'),
            }
        ),
        (
            'Company Info',
            {
                'fields': ('department', 'is_full_time', 'email', 'start_date'),
            }
        ))



@admin.register(NullBlankDemo)
class NullBlankDemoAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
