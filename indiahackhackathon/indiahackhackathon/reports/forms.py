from django.forms import ModelForm
from django import forms
from reports.models import *

# Create the form class.
class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['reporter', 'know_assailant', 'incident_type', 'location',
                  # 'time_of_incident',
                  'date_of_incident', 'description', 'first_name',
                  'last_name','email','phone_number']
        widgets = {
            'date_of_incident': forms.TextInput(attrs={'class': 'datepicker'}),
            # 'time_of_incident': forms.TextInput(attrs={'class': 'datepicker'}),
            'location' : forms.TextInput(attrs={'id':'location'}),
            'first_name' : forms.TextInput(attrs={'placeholder':'Optional'}),
            'last_name' : forms.TextInput(attrs={'placeholder':'Optional'}),
            'email' : forms.TextInput(attrs={'placeholder':'Optional'}),
            'phone_number' : forms.TextInput(attrs={'placeholder':'Optional'}),


        }