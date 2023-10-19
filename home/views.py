from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import RegisterForm
#import xlsxwriter
#import csv
from .models import person, bp_track
from django.contrib.auth import authenticate,login ,logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from django.conf import settings
from django.core.mail import send_mail

from twilio.rest import Client

# Create your views here.

def send_twilio_sms(request):
    sms_message = ("Optum Gamified Solution - se sms aaya ?")
    send_to = [ "+919513341994", ]
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(to=send_to, from_=settings.TWILIO_NUMBER, body=sms_message)
    #return HttpResponse("messages sent!" + message_to_broadcast, 200)
    message = "Congratulations! Message Sent! "
    render(request, 'index.html', context={"message": message })


def index(request):
    message = ""
    if request.method == 'POST':
        print("BP Save aaya")
        sysInput = request.POST.get('sys', None)
        diaInput = request.POST.get('dia', None)
        bpInfo = bp_track(prsn = person.objects.get(user=request.user),sys = sysInput,dia = diaInput)
        #bpInfo.prsn = person.objects.get(user=request.user)
        #bpInfo.sys = sysInput
        #bpInfo.dia = diaInput
        bpInfo.save()
        print("BP Saved")
        message = "Congratulations! You have earned a reward point. BP Details Successfully Saved! "
    return render(request, 'index.html', context={"message": message })


def send_register_email(to_email):
    subject = 'Welcome to Optum-Gamified App'
    msg_html = "Hi.. Thanks for registering at Optum-Gamified App!"
    recipient_list = [to_email, ]
    send_mail( subject, msg_html, settings.EMAIL_HOST_USER, recipient_list )
    return True


def user_profile(request):
    prsn = person.objects.get(user=request.user)
    return render(request, 'profile.html', {'prsn': prsn})


def goals(request):
    return render(request, 'goals.html')

def progress(request):
    return render(request, 'progress.html')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        print("haan")
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #userPass = "A" + str(phone)
            #print("aaya")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #message = "Success: You are now logged in. "
                #uss = request.user
                #print(uss.username + "logged in")
                return redirect('home:profile')
            #else:
               # message = "Error: Invalid Username or Password."
        #else:
            #message = "Error: Invalid Username or Password."
    form = AuthenticationForm()
    return render(  request = request, template_name = "login.html", context={"form": form })


def logout_request(request):
    logout(request)
    #message = "Logged out successfully!"
    #return render(request, 'index.html', {"message": message, })
    return render(request, 'logout.html')


def register(request):
    form1 = RegisterForm()
    if request.method == 'POST':
        userName = request.POST.get('f_name', None)
        phone = request.POST.get('phone', None)
        userPass = "A" + str(phone)
        email = request.POST.get('email', None)
        user1 = User.objects.create_user(username=userName, password=userPass, email=email)
        form1 = RegisterForm(request.POST)
        if form1.is_valid():
            prs = form1.save(False)
            prs.user = user1
            form1.save(True)
            print("Mail sent to -" + email)
            print(send_register_email(email))
            login(request, user1)
            return redirect('home:profile')
        #message = 'ERROR !! Could not register. Please try again. '
        #return render(request,  'person/student_form_adm.html', {'message': message, 'prsn': prsn})
    return render(request, 'user.html', context= {"form": form1 })

