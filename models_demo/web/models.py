from enum import Enum

from django.db import models

# Model fields == Class attributes in Model class


# class EmployeeLevel(Enum):
#     JUNIOR = 'Junior',
#     REGULAR = 'Regular',
#     SENIOR = 'Senior',

class AuditInfoMixin(models.Model):
    class Meta:
        abstract=True

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    # This will be automatically set on each 'save/update'
    updated_on = models.DateTimeField(
        auto_now=True,
    )

class DeletableMixin(models.Model):
    class Meta:
        abstract=True

    is_deleted = models.BooleanField(default=False)

# First create class department(AND MIGRATE),
# and then add it to the other class with ForeignKey(and then MIGRATE AGAIN)
class Department(AuditInfoMixin, models.Model):
    name = models.CharField(
        max_length=15,
    )

    slug = models.SlugField(
        unique=True,
    )

    def __str__(self):
        return f'Id: {self.pk}'

    def get_absolute_url(self):
        pass


class Project(models.Model):
    name = models.CharField(
        max_length=15,
    )


class Employee(models.Model):
    class Meta:

    # правим си вътрешен клас на основния клас Employee,
    # където да добавим мета-данните за него
    # как искаме моделите да бъдат сортирани, ако не им
    # бъде направена допълнителна сортировка
    ordering = ['-age', 'years_of_employment']


    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'
    LEVELS = (
        (LEVEL_SENIOR, LEVEL_SENIOR),
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
    )
    # VARCHAR (30)
    first_name = models.CharField(
        # max_length is REQUIRED argument
        max_length=50,
    )
    # NULL - False by default; if True => empty values will be stored as NULL
    # BLANK - False by default; if True => the field is allowed to be blank
    last_name = models.CharField(
        max_length=50,
        null=True,
    )
    level = models.CharField(
        max_length=50,
        choices=LEVELS,
        #     # DB vs Visualized
        #     ('jr.', 'Junior'),
        #     ('reg.', 'Regular'),
        #     ('sr.', 'Senior'),
        # )
        verbose_name='Seniority Level',
    )
    age = models.IntegerField(
        default=-1,
    )
    years_of_experience = models.PositiveIntegerField()
    review = models.TextField()
    # This will be automatically set on creation
    start_date = models.DateField()
    email = models.EmailField(
        unique=True,
        editable=False,
    )
    # Dropdown menu, being able to choose: 1.Unknown 2.True 3.False
    is_full_time = models.BooleanField(
        null=True,
    )

    #Many-to-One/Each department has many employees/
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    #     CASCADE => изтрий всички emplyees, ако се изтрие department
    #     RESTRICT => не можеш да изтриеш department, ако имаш закачен човек към него
    #     SET_NULL => когато се изтрие department, сет-вай в таблица employee, колона
    #     department на null(работи само, ако Null=True)
    )

    # Many-To-Many/Each employee can be in many project
    # and each project can be handled by many employees
    projects = models.ManyToManyField(
        Project,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        # self.id == self.pk in Models
        return f'ID:{self.pk}/' \
               f'Name:{self.first_name} {self.last_name}/' \




# One-To-One
# Each Employee has only one Access Card


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(
        max_length=15,
    )
    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )


class NullBlankDemo(models.Model):
    blank_true = models.IntegerField(
        blank=True,
        null=False,
    )
    null_true = models.IntegerField(
        blank=False,
        null=True,
    )
    blank_null_true = models.IntegerField(
        blank=True,
        null=True,
    )
    default = models.IntegerField(
        blank=False,
        null=False,
    )
# Methods:
# Employee.objects.all() --> Select *
# Employee.objects.create() --> Insert
# Employee.objects.filter() --> Select * + Where
# Employee.objects.update() --> Update

# Google: Django Raw SQL Log --> to show the generated SQL in Terminal (insert in settings.py)
