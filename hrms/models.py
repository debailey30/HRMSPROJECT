"""
HRMS Models
"""

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    """
    User model that extends the AbstractUser model to include additional fields and relationships.

    Attributes:
        groups (ManyToManyField): The groups this user belongs to. Related to the Group model.
        user_permissions (ManyToManyField): Specific permissions for this user. Related to the Permission model.
        ROLE_CHOICES (tuple): Choices for the role field, including 'admin', 'manager', and 'employee'.
        role (CharField): The role of the user, chosen from ROLE_CHOICES.
        thumb (ImageField): Profile picture of the user, stored in 'profile_pics/' directory.

    Methods:
        (Add any custom methods here)
    """
    groups = models.ManyToManyField(
        Group,
        related_name='hrms_user_set',  # Add related_name to avoid clashes
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='hrms_user_permissions_set',  # Add related_name to avoid clashes
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
    # Add other fields and methods as needed
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    thumb = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

class Employee(models.Model):
    """
    Employee Model
    Attributes:
        GENDER_CHOICES (tuple): Choices for gender field.
        first_name (CharField): First name of the employee, max length 30.
        last_name (CharField): Last name of the employee, max length 30.
        position (CharField): Position of the employee, max length 50.
        phone (CharField): Phone number of the employee, max length 11.
        gender (CharField): Gender of the employee, choices are 'M', 'F', 'O'.
        email (EmailField): Email address of the employee.
        address (TextField): Address of the employee.
        id (AutoField): Primary key, auto-incremented ID of the employee.
        date_of_birth (DateField): Date of birth of the employee.
        department (ForeignKey): Foreign key to the Department model.
    Methods:
        __str__(): Returns a string representation of the employee's name and ID.
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    address = models.TextField()
    id = models.AutoField(primary_key=True)
    date_of_birth = models.DateField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)

    objects = models.Manager()  # Ensure Employee has a default manager

    def __str__(self) -> str:
        """
        Returns a string representation of the employee's name and ID.
        """
        return f"Name: {self.first_name} {self.last_name}, ID: {self.id}"

class Department(models.Model):
    """
    Department model representing a department within the HRMS system.
    Attributes:
        first_name (CharField): The first name of the department head or 
            representative.
        last_name (CharField): The last name of the department head or 
            representative.
        description (TextField): A detailed description of the department.
    Methods:
        __str__(): Returns a string representation of the department, 
            specifically the name.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField()

    objects = models.Manager()  # Ensure Department has a default manager

    def __str__(self):
        """
        Returns a string representation of the department.
        """
        return f'{self.first_name} {self.last_name}'

class Kin(models.Model):
    """
    Kin model to store details of an employee's kin.

    Attributes:
        employee (ForeignKey): The employee to whom the kin is related.
        first_name (CharField): The first name of the kin.
        last_name (CharField): The last name of the kin.
        relationship (CharField): The relationship of the kin to the employee.
        contact_number (CharField): The contact number of the kin.
    Methods:
        __str__(): Returns a string representation of the kin, including their 
            first_name, last_name and relationship
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    relationship = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)

    objects = models.Manager()  # Ensure Kin has a default manager

    def __str__(self):
        """
        Returns a string representation of the kin.
        """
        return f'{self.first_name} {self.last_name} ({self.relationship})'

class Attendance(models.Model):
    """
    Model representing an attendance record for an employee.

 Attributes:
        STATUS_CHOICES (list): A list of tuples representing the possible 
            attendance statuses.
            - 'P': Present
            - 'A': Absent
            - 'L': Late
        status (CharField): The attendance status of the employee. It is a 
            character field with a maximum length of 1 and choices defined 
            by `STATUS_CHOICES`.
        employee (ForeignKey): A foreign key to the Employee model, 
            representing the employee to whom this attendance record belongs.
        date (DateField): The date of the attendance record.

    Methods:
        __str__: Returns a string representation of the attendance record 
            in the format "employee - status".
    """
    STATUS_CHOICES = [
        ('P', 'Present'),
        ('A', 'Absent'),
        ('L', 'Late'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()

    objects = models.Manager()  # Ensure Attendance has a default manager

    def __str__(self):
        """
        Returns a string representation of the attendance record.
        """
        return f"{self.employee} - {self.date} - {self.get_status_display()}"

    def get_status_display(self):
        """
        Returns the display value of the status field.
        """
        return dict(self.STATUS_CHOICES).get(self.status, self.status)

class BusinessCustomization(models.Model):
    """
    BusinessCustomization model represents the customization options 
    for a business entity.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model. 
            When the user is deleted, the associated BusinessCustomization 
            is also deleted.
        logo (ImageField): An optional image field to upload the business logo. 
            The images are stored in the 'business_logos/' directory.
        primary_color (CharField): A string field to store the primary color 
            of the business in hexadecimal format. Defaults to '#000000'.
        secondary_color (CharField): A string field to store the secondary color 
            of the business in hexadecimal format. Defaults to '#FFFFFF'.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='business_logos/', blank=True, null=True)
    primary_color = models.CharField(max_length=7, default='#000000')  # Hex color code
    secondary_color = models.CharField(max_length=7, default='#FFFFFF')  # Hex color code

    objects = models.Manager()  # Ensure BusinessCustomization has a default manager

class Leave(models.Model):
    """
    Model representing a leave request.
    Attributes:
        employee (ForeignKey): Reference to the Employee model. When the 
            referenced employee is deleted, the leave request is also deleted.
        leave_type (CharField): Type of leave requested, with a maximum length 
            of 50 characters.
        start_date (DateField): The start date of the leave.
        end_date (DateField): The end date of the leave.
        documents (FileField): Optional field to upload documents related to 
            the leave, stored in 'leave_documents/' directory.
    Methods:
        __str__(): Returns a string representation of the leave request, 
            showing the employee and the type of leave.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    documents = models.FileField(upload_to='leave_documents/', blank=True, null=True)

    objects = models.Manager()  # Ensure Leave has a default manager

    def __str__(self):
        """
        Returns a string representation of the leave request.
        """
        return f'{self.employee} -> {self.leave_type}'

class EmployeeWarning(models.Model):
    """
    Model representing a warning issued to an employee.
    Attributes:
        employee (ForeignKey): A reference to the Employee model. When the 
            referenced employee is deleted, the warning is also deleted.
        date (DateField): The date when the warning was issued. Automatically 
            set to the current date when the warning is created.
        reason (TextField): The reason for issuing the warning.
    Methods:
        __str__(): Returns a string representation of the warning, including 
            the date and the employee.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    reason = models.TextField()

    objects = models.Manager()  # Ensure EmployeeWarning has a default manager

    def __str__(self):
        """
        Returns a string representation of the warning.
        """
        return f'Warning -> {self.date} -> {self.employee}'

class Recruitment(models.Model):
    """
    Model representing a job recruitment posting.

    Attributes:
        position (CharField): The title of the job position.
        description (TextField): A detailed description of the job position.
        requirements (TextField): The requirements needed for the job position.
        posted_date (DateField): The date when the job posting was created. 
            Automatically set to the current date.
        closing_date (DateField): The date when the job posting will be closed.

    Methods:
        __str__(): Returns the string representation of the Recruitment 
            instance, which is the job position.
    """
    position = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    requirements = models.TextField()
    posted_date = models.DateField(auto_now_add=True)
    closing_date = models.DateField()

    objects = models.Manager()  # Ensure Recruitment has a default manager

    def __str__(self):
        """
        Returns a string representation of the recruitment instance.
        """
        return f"Position: {self.position}, Posted Date: {self.posted_date}, Closing Date: {self.closing_date}"