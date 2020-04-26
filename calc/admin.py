from django.contrib import admin
from .models import BasicChecku,ElectricalChecku,MechanicalChecku,InstallationChecku,ChilledwaterChecku,Name
# Register your models here.
admin.site.register(Name)

admin.site.register(BasicChecku)
admin.site.register(ElectricalChecku)
admin.site.register(MechanicalChecku)
admin.site.register(InstallationChecku)
admin.site.register(ChilledwaterChecku)
