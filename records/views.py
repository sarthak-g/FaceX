# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Records,Files
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewFileForm
from django.views.generic.detail import DetailView
# Create your views here.
def index(request):
    records = Records.objects.all()[:10]    #getting the first 10 records
    context = {
        'records': records
    }
    return render(request, 'records.html', context)

def details(request, id):
    record = Records.objects.get(id=id)
    context = {
        'record' : record
    }
    return render(request, 'details.html', context)
def files(request, id):
    record = Records.objects.get(id=id)
    file = Files.objects.filter(patient_no = id)
    context = {
        'record' : record,
        'file':file,
    }
    return render(request, 'files.html', context)
def newfiles(request,id):
    record = Records.objects.get(id=id)
    if request.method=="POST":
        form = NewFileForm(request.POST)
        if form.is_valid():
            new_req = Files(patient_no=request.POST['patient_id'],pfile=request.POST['patient_text'])
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
