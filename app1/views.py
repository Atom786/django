from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import random
import smtplib
import email.message
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  Registration >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def Register(request):
    if request.POST:
        nm = request.POST['name']
        em = request.POST['email']
        cnt = request.POST['mobileno']
        addr = request.POST['address']
        img1 = request.FILES.get('Photo')
        pass1 = request.POST['pass']
        pass2 = request.POST['cpass']
        try:
            var = Raw_data.objects.get(email=em)
            return HttpResponse("<h1><a href = ""> Already existed</a></h1>")
          #  return render(request, 'login.html')
        except:
            if pass1 == pass2:
                obj = Raw_data()
                obj.name = nm
                obj.email = em
                obj.mobileno = cnt
                obj.address = addr
                obj.password = pass1
                obj.Photo = img1
                obj.save()

            subject = 'Successfully Registration'
            message = f"""Dear, {nm}
            Your Company registration sucessfully. 
            You can login here: http://127.0.0.1:8000/"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [em]
            send_mail(subject, message, email_from, recipient_list)
            print("Successfully sent email")
            return redirect('Login')
        else:
            return HttpResponse("<h1><a href=" "> Password are not Match</a></h1>")
    return render(request, 'Register.html')

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Login >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def Login(request):
    if request.POST:
        email = request.POST['email']
        pass1 = request.POST['pass']
        try:
            var = Raw_data.objects.get(email=email)
            if var.password == pass1:
                request.session['Raw_data'] = var.id
                return redirect('Dashboard')
            else:
                return HttpResponse("<h1><a href=" "> Invalid passwordPassword </a></h1>")
        except:
            return HttpResponse("<h1><a href=" "> Invalid Email id </a></h1>")
    return render(request, 'login.html')


def Logout(request):
    if 'Raw_data' in request.session.keys():
        del request.session['Raw_data']
        return redirect('Login')
    else:
        return redirect('Login')

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Dashboard >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def Dashboard(request):
    if 'Raw_data' in request.session.keys():
        vars = Raw_data.objects.get(id=int(request.session['Raw_data']))
        user = Raw_data.objects.all()
        cords = Customer_orders.objects.filter(comp=vars)
        return render(request, 'Dashboard.html', {'vars': vars, 'user': user, 'cords': cords})
    else:
        return redirect('Login')


def YEsOrder(request, id):
    if 'Raw_data' in request.session.keys():
        cords = Customer_orders.objects.get(id=id)
        cords.status = 'Yes'
        cords.save()
        return redirect('Dashboard')
    else:
        return redirect('Login')


def NoOrder(request, id):
    if 'Raw_data' in request.session.keys():
        cords = Customer_orders.objects.get(id=id)
        cords.status = 'No'
        cords.save()
        return redirect('Dashboard')
    else:
        return redirect('Login')


def View_cus(request):
    if 'Raw_data' in request.session.keys():
        vars = Raw_data.objects.get(id=int(request.session['Raw_data']))
        user = Cus_data.objects.filter(raw=vars)
        return render(request, 'View_cus.html', {'vars': vars, 'user': user})
    else:
        return redirect('Login')


def Add_cus(request):
    if 'Raw_data' in request.session.keys():
        vars = Raw_data.objects.get(id=int(request.session['Raw_data']))
        if request.POST:
            nm = request.POST['name']
            em = request.POST['email']
            cnt = request.POST['Phone']
            addr = request.POST['add1']
            img1 = request.FILES.get('Photo')
            obj = Cus_data()
            obj.raw = vars
            obj.cus_nm = nm
            obj.cus_em = em
            obj.cus_con = cnt
            obj.cus_add1 = addr
            obj.cus_photo = img1
            data = '1234567890'
            pass1 = ""
            for i in range(6):
                pass1 += str(random.choice(data))
            print(pass1)
            obj.cus_pass = pass1
            obj.save()

            subject = 'welcome to Companys world'
            message = f'Dear, {nm} Your  User id is {em} and password is {pass1}  login here: http://127.0.0.1:8000/Cu_login/'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [em]
            send_mail(subject, message, email_from, recipient_list)

            print("Successfully sent email")

            return redirect('View_cus')
        return render(request, 'Add_cus.html', {'vars': vars})
    else:
        return redirect('Login')


def Del_Cus(request, id):
    if 'Raw_data' in request.session.keys():
        cus = Cus_data.objects.get(id=id)
        cus.delete()
        print(cus)
        return redirect('View_cus')
    else:
        return redirect('Login')


def Profile(request):
    if 'Raw_data' in request.session.keys():
        vars = Raw_data.objects.get(id=int(request.session['Raw_data']))

        return render(request, 'Profile.html', {'vars': vars})
    else:
        return redirect('Login')

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Dashboard >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def cu_login(request):
    if request.POST:
        em = request.POST['cus_em']
        ps = request.POST['pass']

        try:
            valid = Cus_data.objects.get(cus_em=em, cus_pass=ps)
            request.session['custom_user'] = valid.id
            return redirect('cu_Home')
        except:
            print("invalid data")
            return redirect('cu_login')
    return render(request, 'cu_login.html')


def cu_Home(request):
    if 'custom_user' in request.session.keys():
        vars = Cus_data.objects.get(id=int(request.session['custom_user']))
        user = Cus_data.objects.all()
        prod = Company_Product.objects.filter(comp=vars.raw)
        return render(request, 'cu_home.html', {'vars': vars, 'prod': prod})
    else:
        return redirect('cu_login')


def Cu_Profile(request):
    if 'custom_user' in request.session.keys():
        vars = Cus_data.objects.get(id=int(request.session['custom_user']))
    return render(request, 'cu_profile.html', {'vars': vars})


def cu_Logout(request):
    if 'Cus_data' in request.session.keys():
        del request.session['Cus_data']
        return redirect('cu_login')
    else:
        return redirect('cu_login')


# ------------------------- product --------------------------

def AddProduct(req):
    if 'Raw_data' in req.session.keys():
        vars = Raw_data.objects.get(id=int(req.session['Raw_data']))

        if req.POST:
            nm = req.POST['nm1']
            pr = req.POST['pr1']
            qty = req.POST['qty1']
            img = req.FILES.get('img1')

            var = Company_Product()
            var.comp = vars
            var.pro_nm = nm
            var.pro_pr = pr
            var.pro_qty = qty
            var.pro_img = img
            var.save()

            return redirect('ViewProduct')
        return render(req, 'add_Product.html', {'vars': vars})
    else:
        return redirect('Login')


def UpdateProduct(req, id):
    if 'Raw_data' in req.session.keys():
        vars = Raw_data.objects.get(id=int(req.session['Raw_data']))
        prod = Company_Product.objects.get(id=id)
        if req.POST:
            nm = req.POST['nm1']
            pr = req.POST['pr1']
            qty = req.POST['qty1']
            img = req.FILES.get('img1')

            prod.comp = vars
            prod.pro_nm = nm
            prod.pro_pr = pr
            prod.pro_qty = qty
            if img != None:
                prod.pro_img = img
            prod.save()

            return redirect('ViewProduct')
        return render(req, 'update_Product.html', {'vars': vars, 'prod': prod})
    else:
        return redirect('Login')


def ViewProduct(req):
    if 'Raw_data' in req.session.keys():
        vars = Raw_data.objects.get(id=int(req.session['Raw_data']))
        prod = Company_Product.objects.filter(comp=vars)
        return render(req, 'View_Product.html', {'vars': vars, 'prod': prod})
    else:
        return redirect('Login')


def DeleteProduct(req, id):
    if 'Raw_data' in req.session.keys():
        prod = Company_Product.objects.get(id=id)
        prod.delete()
        return redirect('ViewProduct')
    else:
        return redirect('Login')


# ------------------------- product ---------------------------


def order_place(request, id):
    if 'custom_user' in request.session.keys():
        cust = Cus_data.objects.get(id=int(request.session['custom_user']))
        prod = Company_Product.objects.get(id=id)
        if request.POST:
            qty1 = request.POST['qty1']
            obj = Customer_orders()
            obj.comp = cust.raw
            obj.cust = cust
            obj.prod = prod
            obj.status = 'False'
            obj.qty = int(qty1)
            obj.tot_price = int(int(qty1) * int(prod.pro_pr))
            obj.save()
            return redirect('view_order')
        return render(request, 'order_place.html', {'prod': prod, 'cust': cust})
    else:
        return redirect('cu_login')


def view_order(request):
    if 'custom_user' in request.session.keys():
        vars = Cus_data.objects.get(id=int(request.session['custom_user']))
        ord = Customer_orders.objects.filter(cust=vars)
        return render(request, 'view_order.html', {'ord': ord, 'vars': vars})

    else:
        return redirect('Login')


def Moreinfo(request, id):
    if 'custom_user' in request.session.keys():
        vars = Cus_data.objects.get(id=int(request.session['custom_user']))
        prod = Company_Product.objects.get(id=id)

        return render(request, 'Moreinfo.html', {'prod': prod, 'vars': vars})
    else:
        return redirect('cu_Home')


def About(request):
    if 'custom_user' in request.session.keys():
        vars = Cus_data.objects.get(id=int(request.session['custom_user']))
        raw = Raw_data.objects.get(id=int(request.session['Raw_data']))
    return render(request, 'About.html', {'vars': vars, 'raw': raw})


def pending(request):
    if 'custom_user' in request.session.keys():
        vars = Cus_data.objects.get(id=int(request.session['custom_user']))
        ord = Customer_orders.objects.filter(cust=vars, status='False')
        return render(request, 'pending.html', {'ord': ord, 'vars': vars})

    else:
        return redirect('Login')


def accept(request):
    if 'custom_user' in request.session.keys():
        vars = Cus_data.objects.get(id=int(request.session['custom_user']))
        ord = Customer_orders.objects.filter(cust=vars, status='Yes')
        return render(request, 'accept.html', {'ord': ord, 'vars': vars})

    else:
        return redirect('Login')


def cancel(request):
    if 'custom_user' in request.session.keys():
        vars = Cus_data.objects.get(id=int(request.session['custom_user']))
        ord = Customer_orders.objects.filter(cust=vars, status='No')
        return render(request, 'cancel.html', {'ord': ord, 'vars': vars})

    else:
        return redirect('Login')


def notice(request):
    if 'custom_user' in request.session.keys():
        vars = Cus_data.objects.get(id=int(request.session['custom_user']))
        user = Cus_data.objects.all()
        prod = Company_Product.objects.filter(comp=vars.raw)
        return render(request, 'cu_dash.html', {'vars': vars, 'prod': prod})
    else:
        return redirect('cu_login')
