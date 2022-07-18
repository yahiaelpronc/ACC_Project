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

def test(req):
    return HttpResponse("yes")


def verify(req,username,dates):
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

    if(myuser != None):
        if(expireDay > 0 or expireMonth > 0 or expireYear > 0):
            didResend=sendEmail(req,myuser.email,resend=True,username=myuser.username)
            if(didResend):
                return HttpResponse("Verfication Expired , Email Resent!")
            else:
                return HttpResponse("Verfication Expired , Resend Failed!")
        else:
            if(myuser.active_status):
                return HttpResponse("Your Account is Already Verified")
            else:
                myuser.active_status=True
                myuser.save()
                return HttpResponse("You Account Has Been Verified!")
    else:
        return HttpResponse("The User You're Trying to Verify Doesn't Exist")


def sendEmail(req,recepient,resend=False,username=None):
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
        link='http://127.0.0.1:8000/final/verify/' + req.POST['username'] + '/' +str(date.today())
        myuser=Myuser.objects.get(username=username)
        myuser.active_link=link
        myuser.save()
        text='hello  '+username+'  please Verify your account here  ' + link
        subject='Animal Care Center Site 2022 By ITI  , ' +req.POST['username']
        mailtext='subject : '+ subject+'\n\n'+text
        server.sendmail(fromaddr,toaddr,mailtext)
        server.quit()
        return True
    link='http://127.0.0.1:8000/final/verify/'+req.POST['username'] +'/'+str(date.today())
    myuser=Myuser.objects.get(username=req.POST['username'])
    myuser.active_link=link
    myuser.save()
    text='hello '+req.POST['username']+'  please Verify your account from here  '+link
    subject='Animal Care Center Site 2022 By ITI , '+req.POST['username']
    mailtext='subject : ' +subject +'\n\n' +text
    server.sendmail(fromaddr,toaddr,mailtext)
    server.quit()




def register(req):
    if(req.method == 'GET'):
        return render(req,'Registration.html')
    else:
        name_reg=r"^[a-zA-Z ,.'-]{4,20}$"
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_regex = r'^01[0125][0-9]{8}$'

        if(re.search(name_reg,req.POST['username']) == None):
            context = {}
            context['errusername'] = 'This Username Is Not Valid, Enter Valid UserName'
            return render(req,'Registration.html',context)

        if(re.search(name_reg,req.POST['firstname']) == None):
            context = {}
            context['errfirstname'] = 'This firstname Is Not Valid, Enter Valid firstname'
            return render(req,'Registration.html',context)

        if(re.search(name_reg,req.POST['lastname']) == None):
            context = {}
            context['errlastname'] = 'This lastname Is Not Valid, Enter Valid lastname'
            return render(req,'Registration.html',context)

        if(re.search(email_regex,req.POST['email']) == None):
            context = {}
            context['erremail'] = 'This email Is Not Valid, Enter Valid email'
            return render(req,'Registration.html',context)


        if(re.search(phone_regex,req.POST['mobile']) == None):
            context = {}
            context['errmobile'] = 'This mobile Is Not Valid, Enter Valid mobile'
            return render(req,'Registration.html',context)
        if(req.POST['password'] != req.POST['confirmpassword']):
            context={}
            context['errnotequal']='confirm password must equal to password'
            return render (req,'Registration.html',context)
        else:

            username=req.POST['username']
            firstname=req.POST['firstname']
            lastname=req.POST['lastname']
            profile_pic=req.FILES['profile_pic']
            email=req.POST['email']
            password=req.POST['password']
            confirmpassword=req.POST['confirmpassword']
            mobile=req.POST['mobile']
            b_date=req.POST['b_date']
            country=req.POST['country']
            face_link=req.POST['face_link']

            myuser=Myuser.objects.create(username=username,firstname=firstname,lastname=lastname,profile_pic=profile_pic,
                              email=email,password=password,mobile=mobile,b_date=b_date,country=country,
                                         face_link=face_link)
            recepient=req.POST['email']
            sendEmail(req,recepient)

            return HttpResponse('inserted')