from django.urls import path,include

from . import views
urlpatterns = [
path('',views.home,name='home'),
path('selection',views.selection,name='selection'),

path('bas',views.bas,name='bas'),
path('chill',views.chill,name='chill'),

path('ele',views.ele,name='ele'),
path('mec',views.mec,name='mec'),
path('inst',views.inst,name='inst'),
path('end',views.end,name='end'),
]