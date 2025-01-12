"""Module for testing HRMS views."""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from hrms.models import Employee, Department
from django.db import models

class ViewTests(TestCase):
    """Test suite for HRMS views."""

    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.department = Department.objects.create(
            first_name='Test',
            last_name='Department',
            description='Test Description'
        )
        self.employee = Employee.objects.create(
            first_name='Test',
            last_name='Employee',
            position='Developer',
            phone='1234567890',
            gender='M',
            email='test@example.com',
            address='123 Test St',
            date_of_birth='1990-01-01',
            department=self.department
        )
        self.kin = Kin.objects.create(
            employee=self.employee,
            first_name='Test',
            last_name='Kin',
            relationship='Brother',
            contact_number='0987654321'
        )

    def test_index_view(self):
        """Test the index view."""
        response = self.client.get(reverse('hrms:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hrms/home/home.html')

    def test_login_view(self):
        """Test the login view."""
        response = self.client.get(reverse('hrms:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hrms/registrations/login.html')

    def test_dashboard_view(self):
        """Test the dashboard view."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('hrms:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hrms/dashboard/index.html')

    def test_employee_list_view(self):
        """Test the employee list view."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('hrms:employee_all'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hrms/employee/index.html')

    def test_employee_detail_view(self):
        """Test the employee detail view."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('hrms:employee_view', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hrms/employee/single.html')

    def test_employee_create_view(self):
        """Test the employee create view."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('hrms:employee_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hrms/employee/create.html')

    def test_employee_update_view(self):
        """Test the employee update view."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('hrms:employee_update', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hrms/employee/edit.html')

    def test_employee_delete_view(self):
        """Test the employee delete view."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('hrms:employee_delete', args=[self.employee.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hrms/employee/confirm_delete.html')

class Kin(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    relationship = models.CharField(max_length=100)

    contact_number = models.CharField(max_length=15)

    objects = models.Manager()  # Add this line to ensure Kin has a default manager