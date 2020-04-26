from django.db import models
from django.forms import ModelForm
from django import forms

class Review(models.Model):

    BasicChecku=models.CharField(max_length=100)
    ElectricalChecku= models.CharField(max_length=100)
    MechanicalChecku=models.CharField(max_length=100)
    InstallationChecku=models.CharField(max_length=100)

    ChilledwaterChecku=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)