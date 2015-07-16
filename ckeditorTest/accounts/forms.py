from django import forms
from django.contrib.auth import get_user_model
from ckeditor.widgets import CKEditorWidget

User = get_user_model()


class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label= "Username", error_messages={'invalid': "Only letters, numbers and underscores Allowed" })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label= "Email address")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label= "Password")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label= "Confirm Password")
    print "Before User type Data"
    role = forms.ChoiceField(widget=forms.Select(attrs=dict(required=True, max_length=30)), choices = ([('seller','seller'), ('buyer','buyer')]),initial= 'seller', required=True,)


    def clean_email(self):
        try:
            user = User.objects.get(username__iexact = self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(" This Email ID is already registered ")


    def clean_username(self):
        try:
            user = User.objects.get(username__iexact = self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(" This Username already exists ")


    def clean_password2(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two passwords did not match ")

        return self.cleaned_data['password2']

    def clean_role(self):
        return self.cleaned_data['role']


class CkEditorForm(forms.Form):

    title = forms.CharField(max_length=100)

    # This loads the awesome_ckeditor (check by id) as defined in the settings.py
    #content = forms.CharField(widget=CKEditorWidget(config_name='awesome_ckeditor'))

    # This loads the default CKEditor as defined in the settings.py
    #content1 = forms.CharField(widget=CKEditorWidget())
