from django.forms import ModelForm
from reports.models import *

# Create the form class.
class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ['reporter', 'know_assailant', 'incident_type', 'location',
                  'time_of_incident', 'date_of_incident', 'description', 'first_name',
                  'last_name','email','phone_number']