from django import forms
from django.contrib.auth.models import User
from .models import SA_Serial_Numbers




class AddAlienware(forms.Form):

    serial_number = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Serial Number", "class":"form-control"}),
		label="")

    location = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Location", "class":"form-control"}),
		label="")

    sa_serial_number = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Student Access Serial Number", "class":"form-control"}),
		label="")

    last_checked = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Date Created", "class":"form-control"}),
		label="")
    
    def clean(self):
        cleaned_data = super().clean()
        # Your custom validation or data processing logic here
        return cleaned_data
    

class AddSparkfun(forms.Form):

    serial_number = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Serial Number", "class":"form-control"}),
		label="")
    
    batch_number = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Batch Number", "class":"form-control"}),
		label="")
    
    location = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Location", "class":"form-control"}),
		label="")

    sa_serial_number = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Student Access Serial Number", "class":"form-control"}),
		label="")

    last_checked = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Date Created", "class":"form-control"}),
		label="")
    
    def clean(self):
        cleaned_data = super().clean()
        # Your custom validation or data processing logic here
        return cleaned_data

class AddTeacherpack(forms.Form):

    serial_number = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Serial Number", "class":"form-control"}),
		label="")
    
    location = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Location", "class":"form-control"}),
		label="")

    sa_serial_number = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Student Access Serial Number", "class":"form-control"}),
		label="")

    last_checked = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Date Created", "class":"form-control"}),
		label="")
    
    def clean(self):
        cleaned_data = super().clean()
        # Your custom validation or data processing logic here
        return cleaned_data
    
class AddRaspberryPiForm(forms.Form):
    
    location = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Location", "class":"form-control"}),
		label="")

    sa_serial_number = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Student Access Serial Number", "class":"form-control"}),
		label="")

    last_checked = forms.CharField(
		required=True, 
		widget=forms.widgets.TextInput(attrs={"placeholder":"Date Created", "class":"form-control"}),
		label="")
    
    def clean(self):
        cleaned_data = super().clean()
        # Your custom validation or data processing logic here
        return cleaned_data
    