from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique = True)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    birthday = models.DateField()
    bloodgroup = models.CharField(max_length=5)
    
    def __str__(self) :
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique = True)
    gender = models.CharField(max_length=10)
    phonenumber = models.IntegerField()
    address = models.CharField(max_length=100)
    birthday = models.DateField()
    bloodgroup = models.CharField(max_length=5)
    
    def __str__(self) :
        return self.name
    
class Appointment(models.Model):
    doctorname = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patientname = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctoremail = models.EmailField(max_length=50, )
    patientemail = models.EmailField(max_length=50)
    appointmentdate = models.DateField()
    appointmenttime = models.TextField()
    symptoms = models.CharField(max_length=100)
    priscription = models.CharField(max_length=100)
    status = models.BooleanField()
    
    
    def __str__(self) :
        return self.patientname+"you have appointment with " + self.doctorname +"on"+self.appointmentdate
