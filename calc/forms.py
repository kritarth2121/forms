from .models import BasicChecku,ElectricalChecku,MechanicalChecku,InstallationChecku,ChilledwaterChecku,Name
from django import forms
from django.forms import widgets

class BasicCheckup(forms.ModelForm):
    class Meta:
        model=BasicChecku
        fields=['description']
        widgets = { 'description': forms.TextInput(attrs={'size': 200})}
class ElectricalCheckup(forms.ModelForm):
    class Meta:
        model=ElectricalChecku
        fields=['description']
        widgets = { 'description': forms.TextInput(attrs={'size': 200})}

class MechanicalCheckup(forms.ModelForm):
    class Meta:
        model=MechanicalChecku
        fields=['description']
        widgets = { 'description': forms.TextInput(attrs={'size': 200})}

class InstallationCheckup(forms.ModelForm):
    class Meta:
        model=InstallationChecku
        fields=['description']
        widgets = { 'description': forms.TextInput(attrs={'size': 200})}

class ChilledwaterCheckup(forms.ModelForm):
    class Meta:
        model=ChilledwaterChecku
        fields=['description']
        widgets = { 'description': forms.TextInput(attrs={'size': 200})}
class Namee(forms.ModelForm):
    class Meta:
        model=Name
        fields=['description']
        widgets = { 'description': forms.TextInput(attrs={'size': 200})}
