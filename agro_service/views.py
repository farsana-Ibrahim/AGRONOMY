from django.shortcuts import render,redirect
from . models import *
from  . forms import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from django.views.generic.detail import DetailView
from farmer.models import *

# Create your views here.
def agro_reg(request):
    global pwd1
    if request.method=="POST":
        agroname=request.POST.get('agroname')
        email=request.POST.get('email')
        mobno=request.POST.get('mobno')
        pwd=request.POST.get('pwd')
        pwd1=request.POST.get('pwd1')
        img=request.FILES.get('img')
        #validation
        value = {
            'agroname': agroname,
            'email': email,
            'mobno': mobno,
            'pwd': pwd
        }
        error_message = None
        
        agro=Agro(agroname=agroname,email=email,mobno=mobno,pwd=pwd,image=img)
        error_message =validateAgro(agro)
        if not error_message:
            agro.save()
            return redirect("msg")
            
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'agro/agro_reg.html', data)
        
 
    return render(request,"agro/agro_reg.html")

def validateAgro(agro):
        error_message = None
        if (not agro.agroname):
            error_message = "Panchayth Name Required !!"
        elif not agro.mobno:
            error_message = 'Phone Number required'
        elif len(agro.mobno) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif (agro.pwd) != pwd1:
            error_message = 'Password Do not match'
        elif len(agro.email) < 5:
            error_message = 'Email must be 5 char long'
        return error_message


def agro_login(request):
    if request.method =="GET":
        return render(request,"agro/agro_login.html")
    else:
        try:
                email = request.POST.get('email')
                pwd = request.POST.get('pwd')
                error_message = None
                agro= Agro.objects.get(email=email)
                if agro and agro.status==1 :
                    print("logged in")
                    if(pwd==agro.pwd):
                        flag=1
                    if flag==1 :
                        request.session['id']=agro.id
                        request.session['email']=agro.email
                        return redirect("agrohome")
                    else:
                        error_message = 'Email or Password invalid !!'
                        return render(request,"agro/agro_login.html",{'error':error_message})
                else:
                    if agro.status==0:
                            error_message="Admin permission required"
                    else:
                        error_message = 'Email or Password invalid !!'
        except Agro.DoesNotExist as e:
                error_message = 'Email or Password invalid !!'
        
        return render(request,"agro/agro_login.html",{'error':error_message})

def msg(request):
    return render(request,"msg.html")

def logout(request):
    del request.session['id']
    messages.info(request,'Agro service Logged out successfully')
    return redirect("/")

def agro_home(request):
    cat=ACateg.objects.filter(agro=request.session['id'])
    return render(request,"agro/agro_home.html",{'cat':cat})

def addCateg(request):
    if request.method=="POST":
        cname=request.POST.get("cname")
        kid=request.POST.get("kid")
        categsave=ACateg(name=cname,agro_id=kid)
        categsave.save()
        return redirect("agrohome")
    return render(request,'agro/addCateg.html')


def Addpro(request):
    if request.method=="POST":
        pname=request.POST.get("pname")
        pdesc=request.POST.get("pdesc")
        stock=request.POST.get("stock")
        price=request.POST.get("price")
        img=request.FILES.get("img")
        cid=request.POST.get("cid")
        kid=request.POST.get("kid")
        plantd=AProducts(pname=pname,pdesc=pdesc,stock=stock,price=price,image=img,category_id=cid,agro_id=kid)
        plantd.save()
        return redirect("agrohome")
    categid =ACateg.objects.filter(agro=request.session['id']) 
    prodview = AProducts.objects.all()
    return render(request, 'agro/Addpro.html',{'cid':categid,'prodview':prodview} )

def allprod(request):
    allp=AProducts.objects.filter(agro=request.session['id'])
    return render(request,'agro/allprod.html',{'allp':allp})



def Cfilter(request,pk):
    cf=AProducts.objects.filter(category=pk)
    return render(request,'agro/Categfilter.html',{'cf':cf})

def status(request):
    acrt=Acart.objects.filter(agro=request.session['id'])
    return render(request,'agro/Upstatus.html',{'acrt':acrt})

def confirmpayment(request,pk):
    Acart.objects.filter(id=pk).update(status=True)
    acrt=Acart.objects.filter(agro=request.session['id'])
    return render(request,'agro/Upstatus.html',{'acrt':acrt})  

def aprodDview(request,did):
    prod=AProducts.objects.get(id=did)
    return render(request,'agro/aproDview.html',{'prd':prod})

def aupprod(request, id):
    prod=AProducts.objects.get(id=id)
    form=AProdforms(request.POST or None,instance=prod)
    if form.is_valid():
        # image_path = prod.image.path
        # if os.path.exists(image_path):
        #     os.remove(image_path)
        form.save()
        return render(request,'agro/aproDview.html',{'prd':prod})
    return render(request, 'agro/aupprod.html', {'prd':prod, 'form':form})

def adelete(request,id):
    prod=AProducts.objects.get(id=id)
    if request.method=='POST':
        prod.delete()
        return redirect('agrohome')
    return render(request,'agro/adelete.html',{'prod':prod}) 
