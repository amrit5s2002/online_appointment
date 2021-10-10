from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.messages.api import error
from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from .models import Appointment, Doctor, Patient
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import MakeAppointmentForm, NewPatientForm, NewUserForm
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def pat_home(request):
     if not request.user.is_active:
         return redirect('loginpage')
     return render(request, 'patienthome.html')


def profile(request):
    if not request.user.is_active:
         return redirect('loginpage')
    Patient_detail = Patient.objects.all().filter(email=request.user)
    d = {'patient_detail': Patient_detail}
    return render(request, 'pateintprofile.html', d)


def register(request):
    if request.method == "POST":
        user_form = NewUserForm(request.POST)
        patient_form = NewPatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            patient = patient_form.save(user = user)
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("homepage")
        else:
            messages.error(request, user_form.errors)
            messages.error(request, patient_form.errors)
    user_form = NewUserForm()
    patient_form =  NewPatientForm()
    return render ( request, template_name="createaccount.html", context={"user_form": user_form, "patient_form": patient_form})


def login_auth(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})


def MakeAppointments(request):
    if not request.user.is_active:
         return redirect('loginpage')
    error = ""
    if not request.user.is_active:
        return redirect('loginpage')
    alldoctors = Doctor.objects.all()
    d = {'alldoctors' : alldoctors }
    if request.method == 'POST':
        doctoremail = request.POST['doctoremail']
        doctorname = request.POST['doctorname']
        patientname = request.POST['patientname']
        patientemail = request.POST['patientemail']
        appointmentdate = request.POST['appointmentdate']
        appointmenttime = request.POST['appointmenttime']
        symptoms = request.POST['symptoms']
        print(request.POST)
        appointment = Appointment.objects.create(doctorname=doctorname, doctoremail=doctoremail,patientname=patientname,patientemail=patientemail,appointmentdate=appointmentdate,appointmenttime=appointmenttime,symptoms=symptoms,status=True,prescription="")
        print(appointment)
        error = "no"
    elif request.method == 'GET':
         return render(request, 'pateintmakeappointments.html',d)

def MakeAppointmentWithForm(request):
    if not request.user.is_active:
         return redirect('loginpage')
    
    if request.method == 'POST':
        appointment_form = MakeAppointmentForm(request.POST)
        if appointment_form.is_valid():
            appointment_form.save(user=request.user)
            messages.success(request, "Appointment successfull" )
            return redirect("homepage")
        else:
            messages.error(request, appointment_form.errors)
            
    appointment_form = MakeAppointmentForm()
    return render ( request, template_name="make_appointment_form.html", context={"appointment_form": appointment_form})


def viewappointments(request):
    if not request.user.is_active:
         return redirect('loginpage')
     
    upcoming_appointments = Appointment.objects.filter(patientname=request.user.patient, appointmentdate__gte=timezone.now()).order_by('appointmentdate')
    print("up-",upcoming_appointments)
    previous_appointments = Appointment.objects.filter(patientname=request.user.patient, appointmentdate__lt=timezone.now()).order_by('-appointmentdate')
    d = {'upcoming_appointments':upcoming_appointments,'previous_appointments':previous_appointments}
    print(d)
    return render(request, 'Patientviewappointments.html',d)

def logout_view(request):
    print(dir(request))
    logout(request)
    return redirect('loginpage')