from django.shortcuts import render,redirect
from django.http import HttpResponse
from store.models import *

# Create your views here.

def login(request):
    return render(request,'login.html')

def log(request):
    a=request.GET['a1']
    b=request.GET['a2']
    x=(a=='admin' and b=='admin')
    if x:
        return render(request,'admin_panel.html')
    else:
        return HttpResponse('Admin not fount')

def dap(request):
    u=product.objects.all()
    return render(request,'dap.html',{'a':u})

def anp(request):
    return render(request,'anp.html')

def ins(request):
    u=product()
    u.name=request.GET['a1']
    u.stock=request.GET['a2']
    u.manufacture=request.GET['a3']
    u.expiry=request.GET['a4']
    u.approval=request.GET['a5']
    u.save()
    return render(request,'anp.html')

def showuser(request):
    u=user.objects.all()
    return render(request,'showuser.html',{'a':u})

def dele(request,id):
    u=user.objects.get(id=id)
    u.delete()
    return redirect('../showuser')

def index(request):
    return render(request ,'index.html')

def edit_stock(request):
    u=product.objects.all()
    return render(request,'edit_stock.html',{'a':u})

def edit(request,id):
    u=product.objects.get(id=id)
    return render(request,'edit.html',{'a':u})

def upd(request,id):
    u=product.objects.get(id=id)
    u.name=request.GET['a1']
    u.stock=request.GET['a2']
    u.manufacture=request.GET['a3']
    u.expiry=request.GET['a4']
    u.approval=request.GET['a5']
    u.save()
    return redirect('../edit_stock')

def delete_stock(request):
    u=product.objects.all()
    return render(request,'delete_stock.html',{'a':u})

def delete(request,id):
    u=product.objects.get(id=id)
    u.delete()
    return redirect('../delete_stock')

def admin_panel(request):
    return render(request,'admin_panel.html')

def aprv_pro(request):
    u=product.objects.all()
    return render(request,'aprv_pro.html',{'a':u})

def apt(request,id):
    u=product.objects.get(id=id)
    u.approval='Yes'
    u.save()
    return redirect('../aprv_pro')

def dapt(request,id):
    u=product.objects.get(id=id)
    u.approval='No'
    u.save()
    return redirect('../aprv_pro')

def only_arpp(request):
    u=product.objects.filter(approval='Yes')
    return render(request,'only_aprp.html',{'a':u})