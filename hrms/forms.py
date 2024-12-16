from django import forms
from .models import Employee, Department, Kin, Attendance, Leave, Recruitment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class RegistrationForm (UserCreationForm):
    """
    RegistrationForm is a Django form for user registration that extends UserCreationForm.
    It includes fields for username, email, password, password confirmation, and a passport photograph.

    Fields:
        username (CharField): A text input field for the username with Bootstrap form-control class and a placeholder.
        email (EmailField): An email input field for the email address with Bootstrap form-control class and a placeholder.
        password1 (CharField): A password input field for the password with Bootstrap form-control class and a placeholder.
        password2 (CharField): A password input field for confirming the password with Bootstrap form-control class and a placeholder.
        thumb (ImageField): An image input field for attaching a passport photograph with Bootstrap form-control class and a label.

    Meta:
        model (User): The user model to be used for this form.
        fields (tuple): The fields to be included in the form.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email is required'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}))
    thumb = forms.ImageField(label='Attach a Passport Photograph',required=True,widget=forms.FileInput(attrs={'class':'form-control mt-2'}))
    class Meta:
        model = get_user_model()
        fields = ('username','email','password1', 'password2','thumb')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':True, 'placeholder':'Username Here', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'}))

class EmployeeForm (forms.ModelForm):
    thumb = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    mobile = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email'}))
    emergency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], widget=forms.Select(attrs={'class':'form-control'}))
    department = forms.ModelChoiceField(Department.objects.all(),required=True, empty_label='Select a department',widget=forms.Select(attrs={'class':'form-control'}))
    language = forms.ChoiceField(choices=[('EN', 'English'), ('FR', 'French')], widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Employee
        fields = '__all__'
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'salary': forms.TextInput(attrs={'class':'form-control'}),
            'bank': forms.TextInput(attrs={'class':'form-control'}),
            'nuban': forms.TextInput(attrs={'class':'form-control'})
        }

class KinForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    employee = forms.ModelChoiceField(Employee.objects.filter(kin__employee=None),required=False,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Kin
        fields = '__all__'
    


class DepartmentForm(forms.ModelForm):
    First_name_ = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department Name'}))
    Last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    history = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Brief Department History'}))
    
    class Meta:
        model = Department
        fields = '__all__'

class AttendanceForm(forms.ModelForm):
    """
    AttendanceForm is a ModelForm for the Attendance model.
    This form includes the following fields:
    - status: A dropdown select field with a CSS class 'form-control'.
    - employee: A dropdown select field with a CSS class 'form-control'.
    - date: A date input field with a CSS class 'form-control'.
    Meta:
        model: The model associated with this form is Attendance.
        fields: The fields included in this form are 'status', 'employee', and 'date'.
        widgets: Custom widgets are used to add CSS classes to the form fields.
    """

    class Meta:
        model = Attendance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
class LeaveForm (forms.ModelForm):

    class Meta:
        model = Leave
        fields = '__all__'

        widgets={
            'start': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'end': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'employee':forms.Select(attrs={'class':'form-control'}),
        }
class RecruitmentForm(forms.ModelForm):
    class Meta:
        model = Recruitment
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

# Ensure the Attendance model is defined in the models file, not here.