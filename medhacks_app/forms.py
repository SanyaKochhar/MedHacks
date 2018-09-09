from django import forms


class DLForm(forms.Form):
    drivers_license = forms.CharField(label='Drivers License Number', max_length=100)