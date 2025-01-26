from .models import Department

def get_departments():

    depts = Department.objects.all().order_by('description')
    return { 'depts':depts}