from django.shortcuts import render
from .forms import AadharForm, OtpaAadharLogin, NewFileForm
from random import randint
from .models import Files, Record
# Create your views here.

def intro(request):
    return render(request,'intro1.html')

def aadharlogin(request):
    if request.method == "GET":
        form = AadharForm()
        return render(request, 'index.html',{'form':form})
    if request.method == "POST":
        form = AadharForm(request.POST)
        import requests
        url = "https://aadhaarverify.p.rapidapi.com/Uidverify"

        querystring = {"uidnumber":request.POST['aadhar_no'],"txn_id":"123456","consent":"Y"}

        payload = ""
        headers = {
        'x-rapidapi-host': "aadhaarverify.p.rapidapi.com",
        'x-rapidapi-key': "4f23e025ddmsh893b101357d4f77p1e07f0jsn57cd65c2d554",
        'content-type': "application/x-www-form-urlencoded"
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

        r = response.json()
        print(r["Succeeded"]["Verify_status"])
        range_start = 10**(3)
        range_end = (10**4)-1
        a = randint(range_start, range_end)
        print("otpa:",a)
        try:
            p = Record(aadhar_no = request.POST['aadhar_no'])
            p.save()
        except Exception as e:
            pass
        return render(request, 'otpa_doctorpanel.html', {'a':a,'a_no':request.POST['aadhar_no']})

    return render(request, 'index.html')


def files(request, id):
    record = Record.objects.get(aadhar_no = id)
    file = Files.objects.filter(aadhar_no = id)
    if not file:
        empty = True
        return render(request, 'files.html', {'empty':empty,'aadhar_num': id})
    else:
        empty = False
        context = {
            'record': record,
            'file':file,
            'empty':empty,
            'aadhar_num': id,
        }

    return render(request, 'files.html', context)




def newfiles(request,id):
    record = Record.objects.get(aadhar_no=id)
    if request.method=="POST":
        form = NewFileForm(request.POST)
        if form.is_valid():
            new_req = Files(aadhar_no=id,date_of_visiting=request.POST.get('date_of_visiting'),symptoms=request.POST.get('symptoms'),drugs=request.POST.get('drugs'),dosage=request.POST.get('dosage'),tests_to_be_done=request.POST.get('tests_to_be_done'),date_for_revisit=request.POST.get('date_for_revisit'))
            new_req.save()
            return render(request,'done.html',{'record':record})
    else:
        file = Files.objects.filter(aadhar_no = id)
        form = NewFileForm()
        context = {
            'form':form,
            'record':record,
            }
        return render(request,'newfile.html',context)



def pharmacy(request):
    number = Record.objects.all()
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
    record = Record.objects.get(aadhar_no=id)
    file = Files.objects.filter(aadhar_no = id)
    context = {
        'record' : record,
        'file':file,
    }
    return render(request,'record_search.html',context)

def patient(request):
    number = Record.objects.all()
    val = number
    context = {
    'number' : number
    }
    return render(request,'patient.html',context)
