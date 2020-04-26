from django.shortcuts import render,redirect
#from .models import BasicChecku,ElectricalChecku,MechanicalChecku,InstallationChecku,ChilledwaterChecku
from .forms import BasicCheckup,ElectricalCheckup,ChilledwaterCheckup,InstallationCheckup,MechanicalCheckup,Namee

# Create your views here.
def home(request):
    return render(request,'index.html')
def selection(request):
    return render(request,'selection.html')
def bas(request):
    if request.method=='POST':
        #b=request.POST.get("b")
        #print(b)
        b=BasicCheckup(request.POST)

        if b.is_valid():
            b.save()
            return redirect('ele')
    else:
        b= BasicCheckup()
    context = {
        'form': b,
    }
    return render(request,'bas.html',context)
def ele(request):
    if request.method=='POST':
        #b=request.POST.get("b")
        #print(b)
        b=ElectricalCheckup(request.POST)

        if b.is_valid():
            b.save()
            return redirect('mec')
    else:
        b= BasicCheckup()
    context = {
        'form': b,
    }
    return render(request,'ele.html',context)
def mec(request):
    if request.method=='POST':

        b=MechanicalCheckup(request.POST)

        if b.is_valid():
            b.save()
            return redirect('inst')
    else:
        b= MechanicalCheckup()
    context = {
        'form': b,
    }
    return render(request,'mec.html',context)
def inst(request):
    if request.method=='POST':

        b=InstallationCheckup(request.POST)

        if b.is_valid():
            b.save()
            return redirect('chill')
    else:
        b= InstallationCheckup()
    context = {
        'form': b,
    }
    return render(request,'inst.html',context)

def chill(request):
    if request.method=='POST':

        b=ChilledwaterCheckup(request.POST)

        if b.is_valid():
            b.save()
            return redirect('end')
    else:
        b= ChilledwaterCheckup()
    context = {
        'form': b,
    }
    return render(request,'chill.html',context)
def end(request):
    if request.method=='POST':

        b=Namee(request.POST)

        if b.is_valid():
            b.save()
            return redirect('end')
    else:
        b= Namee()
    context = {
        'form': b,
    }
    return render(request,'end.html',context)

    
