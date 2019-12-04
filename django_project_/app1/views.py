from django.shortcuts import render
from app1.models import Calate
from django.http import HttpResponse

# Create your views here.

def index (request):
    return render (request, 'index.html')


def CalPage(request):
    return render(request, 'cal.html')


def Cal(request):
    if request.POST: 
        a = request.POST['valueA']
        b = request.POST['valueB']
        result = int(a) + int(b)
        Calate.objects.create(a=a,b=b,result=result)
        
        return render (request, 'result.html', context={'data':result})
    else:
        return HttpResponse('Please vistit us with POST')

def CalList(request):
    data2 = Calate.objects.all()
    return render (request, 'list.html', context={'data':data2})
    #for i in data:
    #    print(i.valueA,i.valueB, data.result)

def Deldata(request):
    Calate.objects.all().delete()
    return HttpResponse('Data deleted')