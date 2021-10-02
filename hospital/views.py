from django.core.checks.messages import Error
from django.shortcuts import render
from .models import*
from django.contrib.auth.models import User,Group

# Create your views here.
def homepage(request):
    return render(request,'index.html') 

def aboutpage(request):
    print("check1")
    return render(request,'about.html')

def loginpage(request):
    print("check2")
    return render(request,'login.html')

def createaccount(request):
    print("check2")
    user = 'none'
    error = ''
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']
        gender = request.POST['gender']
        address = request.POST['address']
        birthday = request.POST['dateofbirth']
        bloodgroup = request.POST['bloodgroup']
        
        
        try:
          if password == repeatpassword:
           Patient.objects.create(name=name,email=email,gender=gender,address = address,birthday = birthday,bloodgroup = bloodgroup)
           user = User.objects.create_user(first_name = name,email = email,password = password,username = email)
           pat_group = Group.objects.get(name = 'Patients')
           pat_group.group.user_set.add(user)
           user.save()
           error = 'no'
          else:
            error = 'yes'
            
        except Exception as e :
            print('An exception occurred')
            
            raise e
            error = 'yes'
    d = {'error':error}
    return render(request,'createaccount.html',d)

