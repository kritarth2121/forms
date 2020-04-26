from django.db import models
from django.forms import ModelForm
from django import forms

class BasicChecku(models.Model):
    description=models.CharField(max_length=100)
class ElectricalChecku(models.Model):
    description=models.CharField(max_length=100)
class MechanicalChecku(models.Model):
    description=models.CharField(max_length=100)
class InstallationChecku(models.Model):
    description=models.CharField(max_length=100)

class ChilledwaterChecku(models.Model):
    description=models.CharField(max_length=100)
class Name(models.Model):
    description=models.CharField(max_length=100)
