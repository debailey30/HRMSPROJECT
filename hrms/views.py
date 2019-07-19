from django.shortcuts import render,redirect, resolve_url,reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models  import AdminProfile,Employee, Department,Kin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView
from .forms import RegistrationForm,LoginForm,EmployeeForm,KinForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.contrib import messages
import json

# Create your views here.
class Index(View):
    def get(self,request):
        return redirect('hrms:login')

#   Authentication
class Register (CreateView):
    model = User
    form_class  = RegistrationForm
    template_name = 'hrms/registrations/register.html'
    success_url = reverse_lazy('hrms:login')
    
class Login_View(LoginView):
    model = User
    form_class = LoginForm
    template_name = 'hrms/registrations/login.html'

    def get_success_url(self):
        query = User.objects.get(adminprofile__user=self.request.user.pk)
        self.request.session['auth_user'] = query.username
        self.request.session['auth_user_thumb'] = query.adminprofile.thumb.url
        url = resolve_url('hrms:dashboard')
        return url

class Logout_View(View):
    def get(self):
        logout(self.request)
        return redirect ('hrms:login',permanent=True)
    
    
 # Main Board   
class Dashboard(LoginRequiredMixin,ListView):
    template_name = 'hrms/dashboard/index.html'
    login_url = 'hrms:login'
    model = User
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        return context

# Employee's Controller
class Employee_New(LoginRequiredMixin,CreateView):
    model = Employee  
    form_class = EmployeeForm  
    template_name = 'hrms/employee/create.html'
    login_url = 'hrms:login'
    redirect_field_name = 'redirect:'
    def get_success_url(self):
        messages.success(self.request, 'Account Created')
        url = reverse_lazy('hrms:employee_all')
        return url
    
class Employee_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/employee/index.html'
    model = Employee
    login_url = 'hrms:login'
    context_object_name = 'employees'

class Employee_View(LoginRequiredMixin,DetailView):
    queryset = Employee.objects.select_related('department')
    template_name = 'hrms/employee/single.html'
    context_object_name = 'employee'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = Kin.objects.get(employee=self.object.pk)
            context["kin"] = query
            return context
        except ObjectDoesNotExist:
            return context
        
class Employee_Update(LoginRequiredMixin,UpdateView):
    template_name = 'hrms/employee/edit.html'
    form_class = EmployeeForm
    model = Employee
    def get_success_url(self):
        messages.success(self.request, 'Profile Updated Successfully')
        url = reverse_lazy('hrms:employee_all')
        return url
    
class Employee_Delete(LoginRequiredMixin,DeleteView):
    pass

class Employee_Kin_Add (CreateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_add.html'
    success_url = reverse_lazy('hrms:employee_view')

    def get_context_data(self):
        context = super().get_context_data()
        if 'id' in self.kwargs:
            emp = Employee.objects.get(pk=self.kwargs['id'])
            context['emp'] = emp
            return context
        else:
            return context

class Employee_Kin_Update(UpdateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_update.html'
    success_url = reverse_lazy('hrms:employee_all')

    def get_initial(self):
        initial = super(Employee_Kin_Update,self).get_initial()
        
        if 'id' in self.kwargs:
            emp =  Employee.objects.get(pk=self.kwargs['id'])
            initial['id_employee'] = emp.first_name
            return initial

#Department views

class Department_Detail(ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    def get_queryset(self): 
        queryset = Employee.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
        return context
    


    


