# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Records,Files
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewFileForm
from django.views.generic.detail import DetailView
from random import randint
# Create your views here.
val = 0
def index(request):
    records = Records.objects.all()[:10]    #getting the first 10 records
    context = {
        'records': records
    }
    return render(request, 'records.html', context)
def pharmacy(request):
    number = Records.objects.all()
    val = number
    context = {
    'number' : number
    }
    return render(request,'pharma.html',context)
def otpa(request):
    range_start = 10**(3)
    range_end = (10**4)-1
    a = randint(range_start, range_end)
    print(a)
    context = {
    'a':a
    }
    return render(request,'otpa.html',context)
def otparecord(request,id):
    # record_s = Records.objects.all()
    # file = Files.objects.all()
    # context = {
    # 'record_s':record_s,
    # 'file':file
    # }
    record = Records.objects.get(id=id)
    file = Files.objects.filter(patient_no = id)
    context = {
        'record' : record,
        'file':file,
    }
    return render(request,'record_search.html',context)
def details(request, id):
    record = Records.objects.get(id=id)
    context = {
        'record' : record
    }
    return render(request, 'details.html', context)
def pdetails(request, id):
    record = Records.objects.get(id=id)
    context = {
        'record' : record
    }
    return render(request, 'pdetails.html', context)
def files(request, id):
    record = Records.objects.get(id=id)
    file = Files.objects.filter(patient_no = id)
    context = {
        'record' : record,
        'file':file,
    }
    return render(request, 'files.html', context)
def pfiles(request, id):
    record = Records.objects.get(id=id)
    file = Files.objects.filter(patient_no = id)
    context = {
        'record' : record,
        'file':file,
    }
    return render(request, 'pfiles.html', context)
def newfiles(request,id):
    record = Records.objects.get(id=id)
    if request.method=="POST":
        form = NewFileForm(request.POST)
        if form.is_valid():
            new_req = Files(patient_no=request.POST['patient_id'],date_of_visiting=request.POST['date_of_visiting'],symptoms=request.POST['symptoms'],drugs=request.POST['drugs'],dosage=request.POST['dosage'],tests_to_be_done=request.POST['tests_to_be_done'],date_for_revisit=request.POST['date_for_revisit'])
            new_req.save()
            return render(request,'done.html',{'record':record})
    else:
        file = Files.objects.filter(patient_no = id)
        form = NewFileForm()
        context = {
            'form':form,
            'record':record,
            }
        return render(request,'newfile.html',context)
