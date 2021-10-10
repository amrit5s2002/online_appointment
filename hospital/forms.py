from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



from .models import Appointment, Patient


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User	
		fields = ['username','email','password1','password2']
        

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class NewPatientForm(forms.ModelForm):
    
	class Meta:
		model = Patient
		fields = [ 'gender', 'phonenumber', 'address', 'birthday', 'bloodgroup']

	def save(self, user, commit=True):
		self.instance.user = user
		return super(NewPatientForm, self).save(commit=commit)

class MakeAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["doctorname", "doctoremail", "appointmentdate", "appointmenttime", "symptoms"]
        widgets = {
			"appointmenttime": forms.TimeInput(attrs={"type": "time"}),
			"appointmentdate": forms.DateInput(attrs={"type": "date"})
		}
        
    def save(self, user, commit=True):
        self.instance.patientname = user.patient
        return super(MakeAppointmentForm, self).save(commit=commit)
        