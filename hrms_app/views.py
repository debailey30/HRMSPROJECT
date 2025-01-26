"""
View for user registration.
View for logging out the user.
    Get context data for the dashboard view.
    Get context data for the dashboard view.
    Get context data for the employee detail view.
    Get context data for the employee update view.
    Get context data for the employee kin add view.
    Get initial data for the employee kin add form.
    Handle GET request for the index page.
Views for the HRMS project.
"""

from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, View, DetailView, TemplateView, ListView, UpdateView, DeleteView
)
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .shared import Employee, Department, Kin, Attendance, Leave, Recruitment
from .forms import RegistrationForm, LoginForm, EmployeeForm, KinForm, DepartmentForm, AttendanceForm, LeaveForm, RecruitmentForm  # Add this line to import AttendanceForm

# Create your views here.
class Index(TemplateView):
    """
    View for the index page.
    """
    template_name = 'hrms/home/home.html'

# Authentication
class Register(CreateView):
    model = get_user_model()
    form_class = RegistrationForm
    template_name = 'hrms/registrations/register.html'
    success_url = reverse_lazy('hrms:login')

def Login_View(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

class Logout_View(View):
    def get(self, request):
        """
        Handle GET request for logging out the user.
        """
        try:
            logout(request)
            messages.success(request, "You have successfully logged out.")
        except ObjectDoesNotExist:
            messages.error(request, "You are not logged in.")
        except AttributeError as e:
            messages.error(request, f"An attribute error occurred: {e}")
        except TypeError as e:
            messages.error(request, f"A type error occurred: {e}")
        except RuntimeError as e:
            messages.error(request, f"A runtime error occurred: {e}")
        return redirect('hrms:login')

# Main Board
class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'hrms/dashboard/index.html'
    login_url = 'hrms:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['admin_count'] = get_user_model().objects.filter(is_staff=True).count()
        context['workers'] = Employee.objects.order_by('-id')
        return context

# Employee's Controller
class Employee_New(LoginRequiredMixin, CreateView):
    """
    View for creating a new employee.
    """
    model = Employee
    form_class = EmployeeForm
    template_name = 'hrms/employee/create.html'
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:employee_all')

class Employee_All(LoginRequiredMixin, ListView):
    """
    View for listing all employees.
    """
    model = Employee
    template_name = 'hrms/employee/index.html'
    login_url = 'hrms:login'
    context_object_name = 'employees'
    paginate_by = 5

class Employee_View(LoginRequiredMixin, DetailView):
    """
    View for displaying detailed information about an employee.
    """
    def get_queryset(self):
        return Employee.objects.select_related('department')
    template_name = 'hrms/employee/single.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = Kin.objects.filter(employee=self.object.pk)
            context["kin"] = query
        except ObjectDoesNotExist:
            messages.warning(self.request, "No emergency contact found for this employee.")
        return context

class Employee_Update(LoginRequiredMixin, UpdateView):
    """
    View for updating an employee.
    """
    model = Employee
    form_class = EmployeeForm
    template_name = 'hrms/employee/edit.html'
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:employee_all')

class Employee_Delete(LoginRequiredMixin, DeleteView):
    """
    View for deleting an employee.
    """
    model = Employee
    template_name = 'hrms/employee/confirm_delete.html'
    success_url = reverse_lazy('hrms:employee_all')
    login_url = 'hrms:login'

class Employee_Kin_Add(LoginRequiredMixin, CreateView):
    """
    View for adding an employee's kin.
    """
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_add.html'
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:employee_all')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'id' in self.kwargs:
            emp = Employee.objects.get(pk=self.kwargs['id'])
            context['emp'] = emp
        return context

class Employee_Kin_Update(LoginRequiredMixin, UpdateView):
    """
    View for updating an employee's kin.
    """
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_update.html'
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:employee_all')

    def get_initial(self):
        initial = super().get_initial()
        if 'id' in self.kwargs:
            emp = Employee.objects.get(pk=self.kwargs['id'])
            initial['employee'] = emp.pk
        return initial

# Department views
class Department_Detail(LoginRequiredMixin, ListView):
    """
    View for displaying detailed information about a department.
    """
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'

    def get_queryset(self):
        queryset = Employee.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["dept"] = Department.objects.get(pk=self.kwargs['pk'])
        except Department.DoesNotExist:
            messages.error(self.request, "Department not found.")
            context["dept"] = None
        return context

class Department_New(LoginRequiredMixin, CreateView):
    """
    View for creating a new department.
    """
    model = Department
    template_name = 'hrms/department/create.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'

class Department_Update(LoginRequiredMixin, UpdateView):
    """
    View for updating a department.
    """
    model = Department
    template_name = 'hrms/department/edit.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')

# Attendance View
class Attendance_New(LoginRequiredMixin, CreateView):
    """
    View for creating a new attendance record.
    """
    model = Attendance
    form_class = AttendanceForm
    login_url = 'hrms:login'
    template_name = 'hrms/attendance/create.html'
    success_url = reverse_lazy('hrms:attendance_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pstaff'] = Attendance.objects.select_related('employee').filter(Q(status='PRESENT') & Q(date=timezone.localdate()))
        return context

class Attendance_Out(LoginRequiredMixin, View):
    """
    View for marking an employee's attendance as out.
    """
    login_url = 'hrms:login'

    def get(self, request):
        try:
            user = Attendance.objects.get(Q(employee__id=self.kwargs['pk']) & Q(status='PRESENT') & Q(date=timezone.localdate()))
            user.last_out = timezone.localtime()
            user.save()
        except Attendance.DoesNotExist:
            messages.error(request, "Attendance record not found.")
        return redirect('hrms:attendance_new')

class LeaveNew(LoginRequiredMixin, CreateView):
    """
    View for creating a new leave record.
    """
    model = Leave
    template_name = 'hrms/leave/create.html'
    form_class = LeaveForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:leave_new')

class LeaveList(LoginRequiredMixin, ListView):
    """
    View for listing all leave records.
    """
    model = Leave
    template_name = 'hrms/leave/list.html'
    login_url = 'hrms:login'
    context_object_name = 'leaves'

class Payroll(LoginRequiredMixin, ListView):
    """
    View for displaying payroll information.
    """
    model = Employee
    template_name = 'hrms/payroll/index.html'
    login_url = 'hrms:login'
    context_object_name = 'stfpay'

class Pay(LoginRequiredMixin, ListView):
    """
    View for displaying pay information.
    """
    model = Employee
    template_name = 'hrms/payroll/index.html'
    context_object_name = 'emps'
    login_url = 'hrms:login'

@login_required(login_url='hrms:login')
def employee_create(request):
    """
    View for creating a new employee.
    """
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('hrms:employee_all')
    else:
        form = EmployeeForm()
    return render(request, 'hrms/employee/employee_form.html', {'form': form})

class RecruitmentNew(LoginRequiredMixin, CreateView):
    """
    View for creating a new recruitment record.
    """
    model = Recruitment
    form_class = RecruitmentForm
    template_name = 'hrms/recruitment/new.html'
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:recruitment_all')

class Recruitment_All(LoginRequiredMixin, ListView):
    """
    View for listing all recruitment records.
    """
    model = Recruitment
    template_name = 'hrms/recruitment/all.html'
    context_object_name = 'recruitments'
    login_url = 'hrms:login'

class RecruitmentDelete(LoginRequiredMixin, DeleteView):
    """
    View for deleting a recruitment record.
    """
    model = Recruitment
    template_name = 'hrms/recruitment/confirm_delete.html'
    success_url = reverse_lazy('hrms:recruitmentall')
    login_url = 'hrms:login'

def recruitment_view_list(request):
    """
    View for displaying recruitment records.
    """
    recruitments = Recruitment.objects.all()
    return render(request, 'hrms/recruitment_list.html', {'recruitments': recruitments})


@login_required(login_url='hrms:login')
def employee_detail(request, pk):
    """
    View for displaying detailed information about an employee.
    """
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'hrms/employee/employee_detail.html', {'employee': employee})

def employee_list(request):
    from .models import Employee
    employees = Employee.objects.all()
    return render(request, 'hrms_app/employee_list.html', {'employees': employees})

def department_list(request):
    from .models import Department
    departments = Department.objects.all()
    return render(request, 'hrms_app/department_list.html', {'departments': departments})

def department_view_list(request):
    from .models import Department
    departments = Department.objects.all()
    return render(request, 'hrms_app/department_list.html', {'departments': departments})
