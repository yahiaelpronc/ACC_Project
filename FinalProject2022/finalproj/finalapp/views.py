from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import json
import smtplib
import socket
from datetime import date
from datetime import datetime, timedelta
from vars import *

import re

# def test(req):
#     return HttpResponse("yes")


def verifyUser(request,username,dates):
    myuser=Myuser.objects.get(username=username)
    date1 = str(dates)
    date1 = dates.split('-')
    # Creation Dates
    CreationDay = int(date1[2])
    CreationMonth = int(date1[1])
    CreationYear = int(date1[0])
    # Expiration Dates
    expireDay = str(date.today())
    expireDay = expireDay.split('-')
    expireDay = int(expireDay[2]) - CreationDay
    expireMonth = str(date.today())
    expireMonth = expireMonth.split('-')
    expireMonth = int(expireMonth[1]) - CreationMonth
    expireYear = str(date.today())
    expireYear = expireYear.split('-')
    expireYear = int(expireYear[0]) - CreationYear

    if(myuser != None ):
        if(expireDay > 0 or expireMonth > 0 or expireYear > 0):
            didResend=sendEmail(request,myuser.email,resend=True,username=myuser.username)
            if(didResend):
                return render(request, 'resendEmail.html')
            else:
                return render(request, 'ResendFailed.html')
        else:
            if(myuser.active_status):
                return render(request, 'alreadyVerified.html')
            else:
                myuser.active_status=True
                myuser.save()
                return render(request, 'successVerified.html')
    else:
        return HttpResponse("The User You're Trying to Verify Doesn't Exist")





def verifyVet(request,username,dates):
    myvet=Vet.objects.get(username=username)
    date1 = str(dates)
    date1 = dates.split('-')
    # Creation Dates
    CreationDay = int(date1[2])
    CreationMonth = int(date1[1])
    CreationYear = int(date1[0])
    # Expiration Dates
    expireDay = str(date.today())
    expireDay = expireDay.split('-')
    expireDay = int(expireDay[2]) - CreationDay
    expireMonth = str(date.today())
    expireMonth = expireMonth.split('-')
    expireMonth = int(expireMonth[1]) - CreationMonth
    expireYear = str(date.today())
    expireYear = expireYear.split('-')
    expireYear = int(expireYear[0]) - CreationYear

    if(myvet != None ):
        if(expireDay > 0 or expireMonth > 0 or expireYear > 0):
            didResend=sendEmail(request,myvet.email,resend=True,username=myvet.username)
            if(didResend):
                return render(request,'resendEmail.html')
            else:
                return render(request, 'ResendFailed.html')

        else:
            if(myvet.active_status):
                return render(request, 'alreadyVerified.html')

            else:
                myvet.active_status=True
                myvet.save()
                return render(request, 'successVerified.html')

    else:
        return HttpResponse("The User You're Trying to Verify Doesn't Exist")

def sendEmail(request,recepient,resend=False,username=None):
    socket.getaddrinfo('localhost',8000)
    fromaddr=settings.EMAIL_HOST_USER
    toaddr=recepient
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.connect("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr,varA)
    if(resend):
        link='http://127.0.0.1:8000/final/verify/' + request.POST['username'] + '/' +str(date.today())
        # myuser=Myuser.objects.get(username=username)
        # myuser.active_link=link
        # myuser.save()
        text='hello  '+username+'  please Verify your account here  ' + link
        subject='Animal Care Center Site 2022 By ITI  , ' +request.POST['username']
        mailtext='subject : '+ subject+'\n\n'+text
        server.sendmail(fromaddr,toaddr,mailtext)
        server.quit()
        return True
    link='http://127.0.0.1:8000/final/verify/'+request.POST['username'] +'/'+str(date.today())
    # myuser=Myuser.objects.get(username=req.POST['username'])
    # myuser.active_link=link
    # myuser.save()
    text='hello '+request.POST['username']+'  please Verify your account from here  '+link
    subject='Animal Care Center Site 2022 By ITI , '+request.POST['username']
    mailtext='subject : ' +subject +'\n\n' +text
    server.sendmail(fromaddr,toaddr,mailtext)
    server.quit()




def sendEmailVet(request,recepient,resend=False,username=None):
    socket.getaddrinfo('localhost',8000)
    fromaddr=settings.EMAIL_HOST_USER
    toaddr=recepient
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.connect("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromaddr,varA)
    if(resend):
        link='http://127.0.0.1:8000/final/verifyVet/' + request.POST['username'] + '/' +str(date.today())
        # myuser=Myuser.objects.get(username=username)
        # myuser.active_link=link
        # myuser.save()
        text='hello  '+username+'  please Verify your account here  ' + link
        subject='Animal Care Center Site 2022 By ITI  , ' +request.POST['username']
        mailtext='subject : '+ subject+'\n\n'+text
        server.sendmail(fromaddr,toaddr,mailtext)
        server.quit()
        return True
    link='http://127.0.0.1:8000/final/verifyVet/'+request.POST['username'] +'/'+str(date.today())
    # myuser=Myuser.objects.get(username=req.POST['username'])
    # myuser.active_link=link
    # myuser.save()
    text='hello '+request.POST['username']+'  please Verify your account from here  '+link
    subject='Animal Care Center Site 2022 By ITI , '+request.POST['username']
    mailtext='subject : ' +subject +'\n\n' +text
    server.sendmail(fromaddr,toaddr,mailtext)
    server.quit()



def registerUser(request):
    if(request.method == 'GET'):
        return render(request,'Registration.html')
    else:
        name_reg=r"^[a-zA-Z ,.'-]{4,20}$"
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_regex = r'^01[0125][0-9]{8}$'

        if(re.search(name_reg,request.POST['username']) == None):
            context = {}
            context['errusername'] = 'This Username Is Not Valid, Enter Valid UserName'
            return render(request,'Registration.html',context)

        if(re.search(name_reg,request.POST['firstname']) == None):
            context = {}
            context['errfirstname'] = 'This firstname Is Not Valid, Enter Valid firstname'
            return render(request,'Registration.html',context)

        if(re.search(name_reg,request.POST['lastname']) == None):
            context = {}
            context['errlastname'] = 'This lastname Is Not Valid, Enter Valid lastname'
            return render(request,'Registration.html',context)

        if(re.search(email_regex,request.POST['email']) == None):
            context = {}
            context['erremail'] = 'This email Is Not Valid, Enter Valid email'
            return render(request,'Registration.html',context)


        if(re.search(phone_regex,request.POST['mobile']) == None):
            context = {}
            context['errmobile'] = 'This mobile Is Not Valid, Enter Valid mobile'
            return render(request,'Registration.html',context)
        if(request.POST['password'] != request.POST['confirmpassword']):
            context={}
            context['errnotequal']='confirm password must equal to password'
            return render (request,'Registration.html',context)
        else:

            username=request.POST['username']
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            profile_pic=request.FILES['profile_pic']
            email=request.POST['email']
            password=request.POST['password']
            confirmpassword=request.POST['confirmpassword']
            mobile=request.POST['mobile']
            b_date=request.POST['b_date']
            country=request.POST['country']
            face_link=request.POST['face_link']

            myuser=Myuser.objects.create(username=username,firstname=firstname,lastname=lastname,profile_pic=profile_pic,
                              email=email,password=password,mobile=mobile,b_date=b_date,country=country,
                                         face_link=face_link)
            recepient=request.POST['email']
            sendEmail(request,recepient)

            return HttpResponse('inserted')


def registervet(request):
    if(request.method == 'GET'):
        return render(request,'registervet.html')
    else:
        name_reg=r"^[a-zA-Z ,.'-]{4,20}$"
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_regex = r'^01[0125][0-9]{8}$'
        address_reg=r"^[a-zA-Z ,.'-]{4,40}$"
        if(re.search(name_reg,request.POST['username']) == None):
            context = {}
            context['errusername'] = 'This Username Is Not Valid, Enter Valid UserName'
            return render(request,'registervet.html',context)
        if (re.search(name_reg, request.POST['firstname']) == None):
            context = {}
            context['errfirstname'] = 'This firstname Is Not Valid, Enter Valid firstname'
            return render(request, 'registervet.html', context)

        if (re.search(name_reg, request.POST['lastname']) == None):
            context = {}
            context['errlastname'] = 'This lastname Is Not Valid, Enter Valid lastname'
            return render(request, 'registervet.html', context)

        if (re.search(email_regex, request.POST['email']) == None):
            context = {}
            context['erremail'] = 'This email Is Not Valid, Enter Valid email'
            return render(request, 'registervet.html', context)

        if (re.search(phone_regex, request.POST['mobile']) == None):
            context = {}
            context['errmobile'] = 'This mobile Is Not Valid, Enter Valid mobile'
            return render(request, 'registervet.html', context)
        if (request.POST['password'] != request.POST['confirmpassword']):
            context = {}
            context['errnotequal'] = 'confirm password must equal to password'
            return render(request, 'registervet.html', context)
        if(re.search(address_reg,request.POST['address']) == None):
            context={}
            context['erraddress']= 'this address is not valid '
            return render(request, 'registervet.html', context)

        else:
            username = request.POST['username']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            profile_pic = request.FILES['profile_pic']
            email = request.POST['email']
            password = request.POST['password']
            mobile = request.POST['mobile']
            b_date = request.POST['b_date']
            country = request.POST['country']
            face_link = request.POST['face_link']
            specialization=request.POST['specialization']
            address=request.POST['address']

            MYvet=Vet.objects.create(username=username,firstname=firstname,lastname=lastname,profile_pic=profile_pic,
                                     email=email,password=password,mobile=mobile,b_date=b_date,country=country,
                                         face_link=face_link,specialization=specialization,address=address)
            recepient = request.POST['email']
            sendEmailVet(request, recepient)

            return HttpResponse('inserted')

def login(request):
    if(request.method == 'GET'):
        return render(request,'login.html')
    else:
        myuser=Myuser.objects.filter(username=request.POST['username'],password=request.POST['password'])
        myvet=Vet.objects.filter(username=request.POST['username'],password=request.POST['password'])

        if(len(myuser) != 0):

            myuser1=Myuser.objects.get(username=request.POST['username'])
            if(myuser1.active_status == False):
                return HttpResponse("this account is not Verified")
            else:
                request.session['username'] = request.POST['username']
                return render(request, 'home.html')
        if(len(myvet) != 0):
            myvet1 = Vet.objects.get(username=request.POST['username'])
            if(myvet1.active_status == False):
                return HttpResponse("this account is not Verified")
            else:
                request.session['username']=request.POST['username']
                return render(request,'home.html')


        else:
            context={}
            context['notfound']='this username and password are not correct'
            return render(request,'login.html',context)










def test(request):
    return render(request,'alreadyVerified.html')



