# Document Title

````markdown
# Code Citations

## License: unknown

<https://github.com/iamdyt/HRMSPROJECT/tree/9a8880bcdc430fb9395bd6092e1eeab66050c0f0/hrms/urls.py>

```python
, name='login'),
    path('logout/', views.Logout_View.as_view(), name='logout'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),

    # Employee Routes
```

## License: unknown

<https://github.com/gerti1991/ProjektiFinal-Python/tree/7c0d8ee94b8b8b900db9d3837b61a91fa61ce2c8/Human_Resource_Management_System_Django/hrms/urls.py>
<https://github.com/gerti1991/ProjektiFinal-Python/tree/7c0d8ee94b8b8b900db9d3837b61a91fa61ce2c8/Human_Resource_Management_System_Django/hrms/urls.py>

```python
('login/', views.Login_View.as_view(), name='login'),
    path('logout/', views.Logout_View.as_view(), name='logout'),
    path('dashboard/', views.Dashboard.as_view
```

## License: unknown

<https://github.com/iamdyt/HRMSPROJECT/tree/9a8880bcdc430fb9395bd6092e1eeab66050c0f0/hrms/views.py>

```python
class Index(TemplateView):
    template_name = 'hrms/home/home.html'

# Authentication
class Register(CreateView):
    model = get_user_model()
    form_class = RegistrationForm
    template_name = 'hrms/registrations/register.html'
    success_url = reverse_lazy('hrms:login')
```

## License: unknown

<https://github.com/MASHON01/Fin/tree/2f8fe69c19c84aebcdf33a8d8ef39ef665d160c4/hrms/views.py>

```python
TemplateView):
    template_name = 'hrms/home/home.html'

# Authentication
class Register(CreateView):
    model = get_user_model()
    form_class = RegistrationForm
    template_name = 'hrms/registrations/register.html'
    success_url = reverse_lazy('hrms:login')
```

## License: unknown

[https://github.com/usamanaveed900/HRMSaas/tree/92424e03aeb9ac2bf1561c0aa31907daf20273ec/hrms/views.py](https://github.com/usamanaveed900/HRMSaas/tree/92424e03aeb9ac2bf1561c0aa31907daf20273ec/hrms/views.py)

```python
] = Leave.objects.all()
        return context

class Payroll(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'hrms/payroll/index.html'
    login_url = 'hrms:login'
    context_object_name = 'stfpay'

class Pay(LoginRequiredMixin, ListView):
    model =
```

