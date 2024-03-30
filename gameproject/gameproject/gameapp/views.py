from django.http import HttpResponse
from django.shortcuts import render
from .models import Game, Team


#from django.shortcuts import render

# Create your views here.

# def index(request):
#   return HttpResponse("Welcome to the GAMING APP")


def home(request):
 #fetch from db:
 obj = Game.objects.all()
 obj1 = Team.objects.all()
 # return HttpResponse("Welcome to the GAMING APP")
 return render(request,"index.html",{'result':obj, 'result1':obj1})

# def about(request):
#     name= "India"
#     return render(request,"about.html",{'obj':name})
#
# def passvalue(request):
#     return render(request,"passvalue.html")
#
# def addition(request):
#     n1=int(request.GET['Num1'])
#     n2=int(request.GET['Num2'])
#     res=n1+n2
#     sub=n1-n2
#     mul=n1*n2
#     div=n1/n2
#     return render(request,"result.html",{'result':res,'sub':sub,'mul':mul,'div':div})
# def contact(request):
#     return HttpResponse("For more details,contact the administrator")
#
# def detail(request):
#     return render(request,"detail.html")
#
# def thanks(request):
#     return HttpResponse("Thank you for choosing our GAMING app")