from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Signup , CurierList
from django.contrib.auth import authenticate, logout,login

# Create your views here.

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user= authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'login.html',d)

def delete_history(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id= request.user.id)
    parcel = CurierList.objects.get(id=pid)
    parcel.delete()
    return redirect('home')


def signup1(request):
    error=""
    if request.method == "POST":
        f = request.POST['firstname']
        l = request.POST['lastname']
        co = request.POST['contact']
        e = request.POST['emailid']
        ci = request.POST['city']
        a = request.POST['address']
        p = request.POST['password']
        try:
            user = User.objects.create_user(username=e, password=p , first_name=f , last_name=l)
            Signup.objects.create(user=user, contact=co, city=ci, address=a)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request,'signup.html',d)


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=""
    if request.method == "POST":
        service = request.POST['delivery_service']
        rname = request.POST['receiver_name']
        rcontact = request.POST['rcontact']
        daddress = request.POST['delivery_address']
        paddress = request.POST['pick_up_address']
        pweight = request.POST['pweight']
        plength = request.POST['plength']
        pwidth = request.POST['pwidth']
        pheight = request.POST['pheight']
        u = User.objects.filter(username=request.user.username).first()

        try:
            CurierList.objects.create(user=u , delivery_service=service,receiver_name=rname , rcontact=rcontact, delivery_address=daddress, pick_up_address=paddress, pweight=pweight, plength=plength ,pwidth=pwidth, pheight=pheight, status='Pending',)

            error = "no"
        except:
            error = "yes"
    user = User.objects.get(id= request.user.id)
    product_list = CurierList.objects.filter(user= user)
    d = {'error':error,'product_list':product_list}
    return render(request,'home.html',d)

def edit_parcel(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    data = CurierList.objects.get(id=pid)
    error= ""
    if request.method == "POST":
        rname = request.POST['receiver_name']
        rcontact = request.POST['rcontact']
        daddress = request.POST['delivery_address']
        paddress = request.POST['pick_up_address']
        pweight = request.POST['pweight']
        plength = request.POST['plength']
        pwidth = request.POST['pwidth']
        pheight = request.POST['pheight']
        try:
            data.receiver_name = rname
            data.rcontact = rcontact
            data.delivery_address = daddress
            data.pick_up_address = paddress
            data.pweight = pweight
            data.plength = plength
            data.pwidth = pwidth
            data.pheight = pheight
            data.save()
            error = "no"
        except:
            error = "yes"
    d = {'data':data,'error':error}
    return render(request,'edit_parcel.html',d)


def assign_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    data = CurierList.objects.get(id=pid)
    error= ""
    if request.method == "POST":
        s = request.POST['status']
        try:
            data.status = s
            data.save()
            error = "no"
        except:
            error = "yes"
    d = {'data':data,'error':error}
    return render(request,'assign_status.html',d)


def all_accept_parcel(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id= request.user.id)
    product_list = CurierList.objects.filter(user=user)
    d = {'product_list':product_list}
    return render(request,'all_accept_parcel.html',d)

def Logout(request):
    logout(request)
    return redirect('login.html')
