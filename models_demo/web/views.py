from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from models_demo.web.models import Employee, Department


def index(request):
    #QuerySet/lazy structure - изпълнява се
    # когато някой иска да я използва/:
    # можем да правим още допълнителни заявки,
    # за да се build-не нашата SQL заявка
    employees = Employee.objects.all()
    employees2 = Employee.objects.filter(department_id=1) \
        .order_by('first_name', 'last_name')
    employees3 = Employee.objects.filter(department__name='Engineering')

    # List
    employees_list = list(employees)

    # Filtering Objects
    employees_aged_35 = Employee.objects.filter(age=35)
    employees_less_than_or_equal_35 = Employee.objects.filter(age__lte=35)
    employees_not_aged_35 = Employee.objects.exclude(age=35)
    employee_with_id_one = Employee.objects.get(id=1)
    employees_aged_35_QuerySet_404 = get_list_or_404(Employee, age=35)
    employees_aged_35_Object_404 = get_object_or_404(Employee, pk=1)
    employees_between_20_and_30_years = Employee.objects.filter(age__range=(20, 30))

    context = {
        'employees': Employee.objects.all(),
        'employees2': Employee.objects.all(),
        # Get returns a SINGLE Object, not a QuerySet
        'department': Employee.objects.get(pk=1),
    }
    return render(request, 'index.html', context)


def delete_employee(request, pk):
    department_pk = 3
    Employee.objects.filter(department_id=department_pk)\
        .delete()
    get_object_or_404(Department, pk=1)\
        .delete()
    return redirect('index')
