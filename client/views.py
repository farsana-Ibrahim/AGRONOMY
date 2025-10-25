import re
from django.test import client
from farmer.models import farmermanage
from farmer.models import *
from .models import *
from django.shortcuts import redirect, render
from django.contrib import messages
from Krishi.settings import RAZORPAY_API_KEY,RAZORPAY_API_SECRET_KEY
import razorpay
global amount
amount=0

def signup(request):
    global pwd1
    if request.method=="POST":
        panchayath=request.POST.get('panchayath')
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobno=request.POST.get('mobno')
        pwd=request.POST.get('pwd')
        pwd1=request.POST.get('pwd1')

        #validation
        value = {
            'panchayath': panchayath,
            'name': name,
            'email': email,
            'mobno': mobno,
            'pwd': pwd
        }
        error_message = None
        
        client=Clientmanage(panchayath=panchayath,name=name,email=email,mobno=mobno,pwd=pwd)
        error_message =validatekrishibhavan(client)
        if not error_message:
            client.save()
            return redirect("index")
            
            
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'client/signup.html', data)
        
        
    return render(request,"client/signup.html")

def validatekrishibhavan(client):
        error_message = None
        
        if (not client.panchayath):
            error_message = "Panchayth Name Required !!"
        elif not client.name:
            error_message = 'Name required'
        elif not client.mobno:
            error_message = 'Phone Number required'
        elif len(client.mobno) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif (client.pwd) != pwd1:
            error_message = 'Password Do not match'
        elif len(client.email) < 5:
            error_message = 'Email must be 5 char long'
        #elif krishi_bhavan.isExists():
            #error_message = 'Email Address Already Registered..'
        # saving

        return error_message
# Create your views here.

def login(request):
    if request.method == "POST":
        try:
            name=request.POST['name']
            pwd=request.POST['pwd']
            clogin = Clientmanage.objects.get(name=name, pwd=pwd)
            request.session['name'] = clogin.name
            request.session['id'] = clogin.id
            messages.success(request,'User logged in successfully')
            return redirect('chome')
        except Clientmanage.DoesNotExist as e:
            messages.info(request, 'username/password invalid..')
            return render(request, "client/login.html")
    return render(request, "client/login.html")        

def chome(request):
    return render(request,'client/chome.html')
def logout(request):
    del request.session['id']
    messages.info(request,'User Logged out successfully')
    return redirect("/")
def echoall(request):
    all=farmermanage.objects.all()
    return render(request,'client/echoall.html',{'all':all})
def echomain(request,id):
    fm=farmermanage.objects.get(id=id)
    print(request.session['id'])
    return render(request,'client/echomain.html',{'fm':fm})
def echoprodall(request,fk):
    prods=EchoProducts.objects.filter(farmer=fk)
    return render(request,'client/echoprodall.html',{'prd':prods})
def eprodDview(request,id):
    if request.method=='POST':
            pname=request.POST.get('pname')
            price=request.POST.get('price')
            img=request.POST.get('img')
            qty=request.POST.get('qty')
            fid=request.POST.get('fid')
            cid=request.POST.get('cid')
            cart=Ecart(name=pname,price=price,image=img,qty=qty,farmer_id=fid,client_id=cid)
            cart.save()
            print(cart)
            return redirect('ecart')
    eprod=EchoProducts.objects.get(id=id)
    return render(request,'client/eprodDview.html',{'prd':eprod})

def ecart(request):
    ecrt=Ecart.objects.filter(client= request.session['id'])
    add=0
    tot=0
    global amount
    for i in ecrt:
        add += i.price * i.qty
        tot=add
        amount=tot
    return render(request,'client/ecart.html',{'ecart':ecrt,'tot':tot,})

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))

def cdelete(request,eid):
    ecrt=Ecart.objects.get(id=eid)  
    if request.method == "POST":
        ecrt.delete()
        return redirect("chome")
    return render(request,'client/cdelete.html')

def razorpay(request):

      global amount
      currency ="INR"
      api_key=RAZORPAY_API_KEY
      amt=int(amount)*100  
      payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
      payment_order_id= payment_order['id']
      return render (request,'client/epay.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})

def echeckout(request,cid):
    global amount
    amt=amount
    clnt=Clientmanage.objects.get(id=cid)
    return render(request,'client/echeckout.html',{'clnt':clnt,'a':amt})

def payondelivery(request):
    return render(request,'client/payondelivery.html')

def orderstatus(request):
    ecrt=Ecart.objects.filter(client=request.session['id'])
    return render(request,'client/ordersts.html',{'ecrt':ecrt})
