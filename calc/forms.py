from .models import Review
from django import forms
from django.forms import widgets

class BasicCheckup(forms.ModelForm):
    class Meta:
        model=Review
        fields=['BasicChecku']
        widgets = { 'BasicChecku': forms.TextInput(attrs={'size': 200})}
class ElectricalCheckup(forms.ModelForm):
    class Meta:
        model=Review
        fields=['ElectricalChecku']
        widgets = { 'ElectricalChecku': forms.TextInput(attrs={'size': 200})}

class MechanicalCheckup(forms.ModelForm):
    class Meta:
        model=Review
        fields=['MechanicalChecku']
        widgets = { 'MechanicalChecku': forms.TextInput(attrs={'size': 200})}

class InstallationCheckup(forms.ModelForm):
    class Meta:
        model=Review
        fields=['InstallationChecku']
        widgets = { 'InstallationChecku': forms.TextInput(attrs={'size': 200})}

class ChilledwaterCheckup(forms.ModelForm):
    class Meta:
        model=Review
        fields=['ChilledwaterChecku']
        widgets = { 'ChilledwaterChecku': forms.TextInput(attrs={'size': 200})}
class Namee(forms.ModelForm):
    class Meta:
        model=Review
        fields=['Name']
        widgets = { 'Name': forms.TextInput(attrs={'size': 200})}
