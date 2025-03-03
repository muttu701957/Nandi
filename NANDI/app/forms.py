# forms.py
from django import forms
from .models import *

class Customer_data(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['user']

class Booking_data(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user']
        
class Payment_data(forms.ModelForm):
    class Meta:
        model = Payment
        exclude = ['user']


class Project_data(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class Executive_data(forms.ModelForm):
    class Meta:
        model = Executive
        exclude = ['user']

class Manager_data(forms.ModelForm):
    class Meta:
        model = Manager
        exclude = ['user']

class Tellicaller_data(forms.ModelForm):
    class Meta:
        model = TelliCaller
        exclude = ['user']
        
class Incntive_executive_Data(forms.ModelForm):
    class Meta:
        model = Incntive_executive
        exclude = ['user']

class Manager_executive_Data(forms.ModelForm):
    class Meta:
        model = Manager_executive
        exclude = ['user']

class Tellicaller_executive_Data(forms.ModelForm):
    class Meta:
        model = Tellicaller_executive
        exclude = ['user']

class billing_m(forms.ModelForm):
    class Meta:
        model = billing_master
        fields= "__all__"