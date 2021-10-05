from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render,HttpResponse
from .models import Doctor, Patient

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def pat_home(request):
    # if not request.user.is_active:
    #     return redirect('loginpage')
    
    # g = request.user.groups.all()[0].name
    # if g == 'Patient':
    return render(request,'patienthome.html')

def profile(request):
    # g = request.user.groups.all()[0].name
    # if g=='Patient':
    #     Patient_detail = Patient.objects.all(filter(email = request.user))
    #     d = {'patient_detail':Patient_detail}
    return render(request,'pateintprofile.html')


def login_auth(request):
    user = None
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        
        user = authenticate(request,username=u,password=p)
        if user is not None:
            login(request,user)
            g = request.user.groups.all()[0].name
            if g=='Patient':
                return HttpResponse('patient logged in successfully')
    return render(request,'login.html')

def MakeAppointments(request):
    all_doctors = Doctor.objects.all()
    d = {"all_doctors":all_doctors}
    return render(request,'patientmakeappointments.html',d)