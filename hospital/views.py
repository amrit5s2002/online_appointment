from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render,HttpResponse
from .models import Appointment, Doctor, Patient
from django.utils import timezone
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def pat_home(request):
    #  if not request.user.is_active:
    #      return redirect('loginpage')
    
    #  g = request.user.groups.all()[0].name
    #  if g == 'Patient':
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
    if request.method =='POST':
        temp = request.POST['doctoremail']
        doctoremail = temp.split()[0]
        doctorname = temp.split()[1]
        Patientname = request.POST['patientname']
        patientemail = request.POST['patientemail']
        Appointmentdate = request.POST['appointmentdate']
        Appointmenttime = request.POST['appointmenttime']
        symptoms = request.POST['symptoms'] 
        try:
            Appointment.objects.create(doctorname=doctorname,doctoremail=doctoremail,Patientname=Patientname,patientemail=patientemail,Appointmenttime=Appointmenttime,Appointmentdate=Appointmentdate,symptoms=symptoms,status=True,prescription="")
            error="no"
        except Exception as e:
            raise e
            error="yes"  
        e ={'error':error}
        return render(request,'patientmakeappointments.html',e)
    return render(request,'patientmakeappointments.html',d)

def viewappointments(request):
    # if not request.user.is_active:
    #      return redirect('loginpage')

    # g = request.user.group.all()[0].name
    # if g == "Patient":
    upcoming_appointments = Appointment.objects.filter(patientemail=request.user,appointmentdate__gte=timezone.now()).order_by('appointmentdate')
    previous_appointments = Appointment.objects.filter(patientemail=request.user,appointmentdate__lt=timezone.now()).order_by('appointmentdate')
    d= {'upcoming_appointments':upcoming_appointments,'previous_appointments':previous_appointments}
    return render(request,'Patientviewappointments.html',d)


