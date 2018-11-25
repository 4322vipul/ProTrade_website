from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .models import Items,ExchangeItems,Feedback
from .forms import ItemForm,ExchangeItemForm,FeedbackForm
from django.conf import settings
# Create your views here.

def login_view(request):
    username=password=''
    username=request.POST.get("username")
    password=request.POST.get("password")
    user=authenticate(request,username=username,password=password)
    
    if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse("home"))
 
    else:
        return render(request,"protrade/login.html",{"message":"Invalid Credentials"})
    
    
    
def home(request):
    return render(request,"protrade/home.html")
'''
    if not request.user.is_authenticated:
        return render(request,"protrade/login.html",{"message":None})
    context={"user":request.user}
'''    
    
   

def buy(request):
    try:
        item=Items.objects.all()
    except Items.DoesNotExist:
        raise Http404("Item does not Exist...")
    context={"item":item}
    return render(request,"protrade/buy.html",context)

def sell(request):

    form=ItemForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        #item=Items.objects.all()
        #context={"item":item}
        return render(request,'protrade/successPage.html')
    context={'form':form}
    
    return render(request,'protrade/sell.html',context)
   
def successPage(request):
    
    return render(request,'successPage.html')


def swap(request):
    form=ExchangeItemForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
                
        a=form.cleaned_data['exchange_item_price']

        item=Items.objects.filter(item_price=a).all()
        b=Items.objects.filter(item_price=a).all().count()
        context={"item":item}
        if b==0:
            return render(request,"protrade/validItems.html",{"message":"Sorry no item found with similar price!!"})
        else:
            return render(request,"protrade/validItems.html",context)
        
        
    context={'form':form}    
    return render(request,"protrade/swap.html",context)
        
def contacts(request):
    form=FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request,'protrade/feedbackSuccessPage.html')
    
    context={'form':form}     
    return render(request,"protrade/contacts.html",context)

def feedbackSuccessPage(request):
    return render(request,'feedbackSuccessPage.html')

def logout_view(request):
    logout(request)
    return render(request,"protrade/login.html",{"message":"Logged Out."})