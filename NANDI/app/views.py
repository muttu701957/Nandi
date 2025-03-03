from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
def Loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request, 'Main/home.html')
        else:
            messages.error(request,"Invalid username or password")  
            return render(request, 'Main/Login.html')
    return render(request, 'Main/Login.html')

@login_required(login_url="login")
def home(request):
    user = request.user
    group = user.groups.filter(name="Accounts").exists(),
    return render(request, 'Main/home.html', {"group":group})

def index(request):
    return render(request ,'Main/index.html')

# Customer
def Logout(request):
    logout(request)
    return redirect("login")
# Customer list
@login_required(login_url="login")
def customer_list(request):
    try:
        user=request.user
        if user.groups.filter(name="Admin").exists():
            cust = Customer.objects.all()
            return render(request, 'Customer/customer_list.html',{'customers':cust})
        else:
            cust = Customer.objects.filter(user = request.user)
            return render(request, 'Customer/customer_list.html',{'customers':cust})
    except:
        messages.error(request,"Failed to Show the list of Customer")
    return redirect("home")
# customer add
@login_required(login_url="login")
def customer_add(request):
    try:
        if request.method == 'POST':
            form = Customer_data(request.POST)
            if form.is_valid():
                c=form.save(commit=False)
                c.user = request.user
                c.save()
                messages.success(request, "Data Stored Successfully!")
                return redirect('customer_list')  
        else:
            form = Customer_data()
        return render(request, 'Customer/customer_add.html')
    except:
        messages.error(request,'Failed to Store Data')
    redirect('customer_list')


# customer edit
@login_required(login_url="login")
def customer_edit(request, id):
    try:
        customer_list = get_object_or_404(Customer, id=id)
        if request.method == 'POST':
            form = Customer_data(request.POST, instance=customer_list)
            if form.is_valid():
                form.save()
                messages.success(request, 'Data Updated Successfully!')
                return redirect('customer_list')
            else:
                return render(request, 'Customer/customer_edit.html', {'form': form})
        form = Customer_data(instance=customer_list)        
        return render(request, 'Customer/customer_edit.html', {'form': form})
    except:
        messages.error(request,"Failed to Update the Data.")
    return redirect('customer_list')

# customer delete
@login_required(login_url="login")
def customer_delete(request, id):
    try:
        customer = get_object_or_404(Customer, id=id)
        customer.delete()
    except:
        messages.error(request, 'Failed to delete the Data.')
    finally:
        messages.success(request, 'Data Deleted Successfully!')
    return redirect('customer_list')

# Booking

# booking list
@login_required(login_url="login")
def Booking_list(request):
    try:
        user=request.user
        if user.groups.filter(name="Admin").exists():
            book = Booking.objects.all()
            return render(request, 'Booking/Booking_list.html',{'Book':book})
        else:
            book = Booking.objects.filter(user = request.user)
            return render(request, 'Booking/Booking_list.html',{'Book':book})
    except:
        messages.error(request,"Failed to Show the list of Booking")
    return redirect("home")
# booking add
@login_required(login_url="login")
def Booking_add(request):
        try:
        if request.method == 'POST':
            form = Booking_data(request.POST)
            form1 =billing_m()
            if form.is_valid():
                c=form.save(commit=False)
                c.user = request.user
                c.save()
                return redirect('Booking_list')
                messages.success(request,"Data Stored Successfully!") 
        else:
            user=request.user
            if user.groups.filter(name="Admin").exists():
                cust = Customer.objects.all()
                return render(request, 'Booking/Booking_add.html',{'cust':cust})
            else:
                cust = Customer.objects.filter(user = request.user)
                return render(request, 'Booking/Booking_add.html',{'cust':cust})
    except :
        messages.error(request,"Failed To Store Data")
        return redirect('Booking_list')

# booking edit
@login_required(login_url="login")
def Booking_edit(request,id):
    try:
        Booking_list=get_object_or_404(Booking ,id=id)
        if request.method =='POST':
            update = Booking_data(request.POST , instance=Booking_list)
            if update.is_valid():
                update.save()
                return redirect(reverse('Booking_list'))
            else:
                return render(request, 'Booking/Booking_edit.html' ,{"form":update})
        else:
            update =Booking_data(instance=Booking_list)
        messages.success(request,"Data Updated Successfully!")
        return render(request, 'Booking/Booking_edit.html', {"form":update})
    except:
         messages.error(request,"Failed to Update the Data.")
    return redirect('Booking_list')

# booking delete
@login_required(login_url="login")
def Booking_delete(request,id):
    try:
        delbook =get_object_or_404(Booking,id=id)
        delbook.delete()
    except:
        messages.error(request,"Failed to Delete the Data.")
    finally:
        messages.success(request, 'Data Deleted Successfully!')
    return redirect('Booking_list')

# Booking view
@login_required(login_url="login")
def booking_view(request,id):
    book=get_object_or_404(Booking,id=id)
    return render(request,'Booking/booking_view.html',{'form':book})


# Recipt

# recipt list
@login_required(login_url="login")
def reciept_list(request):
    try:
        user=request.user
        if user.groups.filter(name="Admin")|user.groups.filter(name="Accounts"):
            paylist=Payment.objects.all()
            return render(request ,'Payment/reciept_list.html',{'payment':paylist})
        else:
            paylist = Payment.objects.filter(user = request.user)
            return render(request ,'Payment/reciept_list.html',{'payment':paylist})
    except:
        messages.error(request,"Failed to Show the list of Recipt")
    return redirect('home')

# payment add
@login_required(login_url="login")
def pay_add(request):
    try:
        if request.method == "POST":
            form = Payment_data(request.POST)
            if form.is_valid():
                c=form.save(commit=False)
                c.user = request.user
                c.save()
                messages.success(request,"Data Stored Successfully!")
                return redirect(reverse('reciept_list'))
        else:
            user=request.user
            if user.groups.filter(name="Admin").exists():
                cust = Booking.objects.all()
                return render(request, 'Payment/pay_add.html',{'cust':cust})
            else:
                cust = Booking.objects.filter(user = request.user)
                return render(request, 'Payment/pay_add.html',{'cust':cust})
    except:
        messages.error(request,"Failed to Store the Data.")
    return redirect('reciept_list')

# approval payment
def A_list(request):
    try:
        user=request.user
        if user.groups.filter(name="Admin")|user.groups.filter(name="Accounts"):
            paylist=Payment.objects.filter(status="Pending")|Payment.objects.filter(status="Decline")
            return render(request ,'Payment/Approval_list.html ',{'payment':paylist})
        else:
            payl = Payment.objects.filter(user = request.user)
            paylist =payl.filter(status="pending")
            return render(request ,'Payment/Approval_list.html',{'payment':paylist})
        
    except:
        messages.error(request,"Failed to Show the list of Recipt")
    return redirect('home')
# approval Permission
def Approval_permit(request,id):
    try:
        pay=get_object_or_404(Payment ,id=id)
        if request.method =='POST':
            update = Payment_data(request.POST , instance=pay)
            if update.is_valid():
                update.save()
                messages.success(request,"Data Approved Successfully!")
                return redirect(reverse('A_list'))
            else:
                return render(request, 'Payment/Approval_permit.html' ,{"form":update})
        else:
            update =Payment_data(instance=pay)
        return render(request, 'Payment/Approval_permit.html', {"form":update})
    except:
          messages.error(request,"Failed to Update the Data.")
    return redirect("A_list")

def ledger_view(request,id):
    book =get_object_or_404(Booking,id=id)
    pay = Payment.objects.filter(bill_no=id)&Payment.objects.filter(status="Approved")
    balance_Amount =int(book.tamount)-int(book.book_amt)
    tpl=[]
    payledger={
        "dt": book.dt,
        "p_mode":book.p_mode,
        "book_amt":book.book_amt,
        "balance":balance_Amount
    }
    tpl.append(payledger)
    for i in pay:
        balance_Amount =balance_Amount-int(i.book_amt)
        payledger={
            "dt": i.dt,
            "p_mode":i.p_mode,
            "book_amt":i.book_amt,
            "balance":balance_Amount,
        }
        tpl.append(payledger)
    payledglist={
        "info":{
            "name":book.fname,
            "flat":book.flt,
            "p_name":book.p_name,
            "sqft":book.sqft,
            "rate":book.rate,
            "tamount":book.tamount,
        },
        "tpl":tpl
    }
    return render(request,"Payment/ledger_view.html",{'payledglist':payledglist})

@login_required(login_url="login")
def pay_edit(request ,id):
    try:
        pay_list =get_object_or_404(Payment,id=id)
        if request.method =="POST":
            update =Payment_data(request.POST , instance=pay_list)
            if update.is_valid():
                update.save()
                messages.success(request,"Data Updated Successfully!")
                return  redirect('reciept_list')
        update =Payment_data(instance=pay_list)
        return render(request,'Payment/pay_edit.html',{'pay':update})
    except:
        messages.error(request,"Failed to Store the Data.")
    return redirect("reciept_list")

# ledger 
@login_required(login_url="login")
def ledger(request):
    book=Booking.objects.all()
    return render(request,'Payment/ledger.html',{'book':book})
@login_required(login_url="login")
def pay_view(request):
    return render(request,'Payment/pay_view.html')

# Follow Up
@login_required(login_url="login")
def follow_up(request):
    return render(request,'Follow Up/follow_up.html')

# Incentive
# report
@login_required(login_url="login")
def customer_report(request):
    return render(request,"Report/customer_report.html")
@login_required(login_url="login")
def payment_report(request):
    if request.method == "POST":
        name=request.POST.get('fname')
        tdate=request.POST.get('tdate')
        fdate=request.POST.get('fdate')
        fdata=Payment.objects.filter(fname=name)
        fromdata = fdata.filter(dt__gte=fdate, dt__lte=tdate)
        return render(request,"Report/payment_report.html",{'book':fromdata})
    return render(request,"Report/payment_report.html")
@login_required(login_url="login")
def Booking_report(request):
    if request.method == "POST":
        name=request.POST.get('fname')
        tdate=request.POST.get('tdate')
        fdate=request.POST.get('fdate')
        fdata=Booking.objects.filter(fname=name)
        fromdata = fdata.filter(dt__gte=fdate, dt__lte=tdate)
        return render(request,"Report/Booking_report.html",{'book':fromdata})
    return render(request,"Report/Booking_report.html")
@login_required(login_url="login")
def Executve_report(request):
    return render(request,"Report/Executve_report.html")
@login_required(login_url="login")
def manager_report(request):
    return render(request,"Report/manager_reprot.html")
@login_required(login_url="login")
def Tellicaller_report(request):
    return render(request,"Report/Tellicaller_report.html")
# Executive
@login_required(login_url="login")
def ex_pay_add(request):
    try:
        if request.method == 'POST':
            form = Incntive_executive_Data(request.POST)
            if form.is_valid():
                c=form.save(commit=False)
                c.user = request.user
                c.save()
                messages.success(request, "Data Stored Successfully!")
                return redirect('incetive_executive')    
        return render(request, 'Incentive/ex_pay_add.html')
    except:
        messages.error(request,'Failed to Store Data')
    redirect('incetive_executive')
@login_required(login_url="login")
def ex_pay_edit(request,id):
    try:
        pay_list =get_object_or_404(Incntive_executive,id=id)
        if request.method =="POST":
            update =Incntive_executive_Data(request.POST , instance=pay_list)
            if update.is_valid():
                update.save()
                messages.success(request,"Data Updated Successfully!")
                return  redirect('incetive_executive')
        update =Incntive_executive_Data(instance=pay_list)
        return render(request,'Incentive/ex_pay_edit.html',{'update':update})
    except:
        messages.error(request,"Failed to Store the Data.")
    return redirect("incetive_executive")
# Manager
@login_required(login_url="login")
def m_pay_add(request):
    try:
        if request.method == 'POST':
            form = Manager_executive_Data(request.POST)
            if form.is_valid():
                c=form.save(commit=False)
                c.user = request.user
                c.save()
                messages.success(request, "Data Stored Successfully!")
                return redirect('incetive_manager')    
        return render(request, 'Incentive/m_pay_add.html')
    except:
        messages.error(request,'Failed to Store Data')
    redirect('incetive_manager')
@login_required(login_url="login")
def m_pay_edit(request,id):
    try:
        pay_list =get_object_or_404(Manager_executive,id=id)
        if request.method =="POST":
            update =Manager_executive_Data(request.POST , instance=pay_list)
            if update.is_valid():
                update.save()
                messages.success(request,"Data Updated Successfully!")
                return  redirect('incetive_manager')
        update =Manager_executive_Data(instance=pay_list)
        return render(request,'Incentive/m_pay_edit.html',{'update':update})
    except:
        messages.error(request,"Failed to Store the Data.")
    return redirect("incetive_manager")
# Tellicaller
@login_required(login_url="login")
def t_pay_add(request):
    try:
        if request.method == 'POST':
            form = Tellicaller_executive_Data(request.POST)
            if form.is_valid():
                c=form.save(commit=False)
                c.user = request.user
                c.save()
                messages.success(request, "Data Stored Successfully!")
                return redirect('incentive_tellicaller') 
            return redirect('t_pay_add')
        return render(request, 'Incentive/t_pay_add.html')
    except:
        messages.error(request,'Failed to Store Data')
    redirect('incentive_tellicaller')
@login_required(login_url="login")
def t_pay_edit(request,id):
    try:
        pay_list =get_object_or_404(Tellicaller_executive,id=id)
        if request.method =="POST":
            update =Tellicaller_executive_Data(request.POST , instance=pay_list)
            if update.is_valid():
                update.save()
                messages.success(request,"Data Updated Successfully!")
                return  redirect('incentive_tellicaller')
        update =Tellicaller_executive_Data(instance=pay_list)
        return render(request,'Incentive/t_pay_edit.html',{'update':update})
    except:
        messages.error(request,"Failed to Store the Data.")
    return redirect("incentive_tellicaller")
#  project
@login_required(login_url="login")
def incetive_executive(request):
    user=request.user
    if user.groups.filter(name="Admin").exists():
        exe=Incntive_executive.objects.all()
        return render(request,'Incentive/incetive_executive.html',{'executive':exe})
    else:
        exe = Incntive_executive.objects.filter(user = request.user)
        return render(request,'Incentive/incetive_executive.html',{'executive':exe})
    
# executive
@login_required(login_url="login")
def incetive_manager(request):
    user=request.user
    if user.groups.filter(name="Admin").exists():
        incentive_manager =Manager_executive.objects.all()
        return render(request,'Incentive/incetive_manager.html',{'manager':incentive_manager})
    else:
        incentive_manager = Manager_executive.objects.filter(user = request.user)
        return render(request,'Incentive/incetive_manager.html',{'manager':incentive_manager})
    
# telicaller
@login_required(login_url="login")
def incentive_tellicaller(request):
    user=request.user
    if user.groups.filter(name="Admin").exists():
        incentive_telli =Tellicaller_executive.objects.all()
        return render(request,'Incentive/incentive_tellicaller.html',{"telli":incentive_telli})
    else:
        incentive_telli = Tellicaller_executive.objects.filter(user = request.user)
        return render(request,'Incentive/incentive_tellicaller.html',{"telli":incentive_telli})

# Agreement
@login_required(login_url="login")
def nandi_plot(request):
    return render(request,'Agreement/nandi_plot.html')
@login_required(login_url="login")
def nandi_flat(request):
    return render(request,'Agreement/nandi_flat.html')

# Call Back @login_required(login_url="login")
def call_back(request):
    return render(request,"Call Back/call_back.html")

# Store Master
# Project

# project list
@login_required(login_url="login")
def project_list(request):
    try:
        user=request.user
        if user.groups.filter(name="Admin").exists():
            project =Project.objects.all()
            return render(request, 'Store Master/project_list.html',{'project':project})
        else:
            project = Project.objects.filter(user = request.user)
            return render(request, 'Store Master/project_list.html',{'project':project})
    except:
        messages.error(request,"Failed to Show the list of Project")
    return redirect('home')

# project add
@login_required(login_url="login")
def project_add(request):
    try:
        if request.method == 'POST':
            form =Project_data(request.POST)
            if form.is_valid():
                c=form.save(commit=False)
                c.user = request.user
                c.save()
                messages.success(request,"Data Store Successfully!")
                return redirect('project_list')
        return render(request, 'Store Master/project_add.html')
    except:
        messages.error(request,"Failed to Store the Data.")
    return redirect('project_list')


# project edit
@login_required(login_url="login")
def project_edit(request,id):
    try:
        project_list = get_object_or_404(Project,id=id)
        if request.method == 'POST':
            update = Project_data(request.POST ,instance=project_list)
            if update.is_valid():
                update.save()
                messages.success(request,"Data Updated Successfully!")
                return redirect('project_list')
        update=Project_data(instance=project_list)
        return render(request,'Store Master/project_edit.html' ,{'project':update})
    except:
        messages.error(request,"Failed to Update the Data.")
    return redirect('project_list')

# project delete
@login_required(login_url="login")
def project_delete(request,id):
    try:
        delbook =get_object_or_404(Project,id=id)
        delbook.delete()
    except:
        messages.error(request,"Failed to Delete the Data.")
    finally:
        messages.success(request,"Data Deleted Successfully!")
    return redirect('project_list')

# Executive

# executive list
@login_required(login_url="login")
def ex_list(request):
    try:
        user=request.user
        if user.groups.filter(name="Admin").exists():
            executive =Executive.objects.all()
            return render(request, 'Store Master/ex_list.html',{'executive':executive})
        else:
            executive = Executive.objects.filter(user = request.user)
            return render(request, 'Store Master/ex_list.html',{'executive':executive})
    except:
        messages.error(request,"Failed to Show the list of Executive")
    return redirect('home')
#excutive add
@login_required(login_url="login")
def ex_add(request):
    try:
        if request.method == 'POST':
            form =Executive_data(request.POST)
            if form.is_valid():
                c=form.save(commit=False)
                c.user = request.user
                c.save()
                messages.success(request, "Data Stored Successfully!")
                return redirect('ex_list')
        return render(request, 'Store Master/ex_add.html')
    except:
        messages.error(request,"Failed to Store the Data.")
    return redirect('ex_list')
# executive edit
@login_required(login_url="login")
def ex_edit(request,id):
    try:
        executive_list = get_object_or_404(Executive,id=id)
        if request.method == 'POST':
            update = Executive_data(request.POST ,instance=executive_list)
            if update.is_valid():
                update.save()
                messages.success(request,"Data Updated Successfully")
                return redirect('ex_list')
        update=Executive_data(instance=executive_list)
        return render(request,'Store Master/ex_edit.html' ,{'update':update})
    except:
        messages.error(request,"Failed to Update the Data.")
    return redirect('ex_list')
# executive delete
@login_required(login_url="login")
def ex_delete(request,id):
    try:
        delexecutive =get_object_or_404(Executive,id=id)
        delexecutive.delete()
    except:
        messages.error(request,"Failed to Delete the Data.")
    finally:
        messages.success(request,"Data Delete Successfully!")
    return redirect('ex_list')

#  Manager

# manager list

@login_required(login_url="login")
def m_list(request):
    try:
        user=request.user
        if user.groups.filter(name="Admin").exists():
            manager =Manager.objects.all()
            return render(request, 'Store Master/m_list.html',{'manager':manager})
        else:
            manager = Manager.objects.filter(user = request.user)
            return render(request, 'Store Master/m_list.html',{'manager':manager})
        
    except:
        messages.error(request,"Failed to Show the list of Manager")
    return redirect('home')

# manager add
@login_required(login_url="login")
def m_add(request):
    try:
        if request.method == 'POST':
            form =Manager_data(request.POST)
            if form.is_valid():
                c=form.save(commit=False)
                c.user = request.user
                c.save()
                messages.success(request,"Data Stored Successfully!")
                return redirect('m_list')
        return render(request, 'Store Master/m_add.html')
    except:
        messages.error(request,"Failed to Store the Data.")
    return redirect('m_list')

# manager edit
@login_required(login_url="login")
def m_edit(request,id):
    try:
        manager_list = get_object_or_404(Manager,id=id)
        if request.method == 'POST':
            update = Manager_data(request.POST ,instance=manager_list)
            if update.is_valid():
                update.save()
                messages.success(request,"Data Updated Successfully!")
                return redirect('m_list')
        update=Manager_data(instance=manager_list)
        return render(request,'Store Master/m_edit.html' ,{'update':update})
    except:
        messages.error(request,"Failed to Update the Data.")

# manager delete
@login_required(login_url="login")
def m_delete(request,id):
    try:
        delman =get_object_or_404(Manager,id=id)
        delman.delete()
    except:
        messages.error(request,"Failed to Delete the Data.")
    finally:
        messages.success(request,"Data Deleted Successfully!")
    return redirect('m_list')

#  Tellicaller

# relicaller list
@login_required(login_url="login")
def t_list(request):
    try:
        user=request.user
        if user.groups.filter(name="Admin").exists():
            telli =TelliCaller.objects.all()
            return render(request, 'Store Master/tel_list.html',{'telli':telli})
        else:
            telli = TelliCaller.objects.filter(user = request.user)
            return render(request, 'Store Master/tel_list.html',{'telli':telli})
    except:
        messages.error(request,'Failed to Show the list of Telicaller')
        return redirect("home")

# telicaller add
@login_required(login_url="login")
def t_add(request):
    try:
        if request.method == 'POST':
            form =Tellicaller_data(request.POST)
            if form.is_valid():
                c=form.save(commit=False)
                c.user = request.user
                c.save()
                messages.success(request,'Data store Successfully!')
                return redirect('t_list')
        return render(request, 'Store Master/tel_add.html')
    except:
        messages.error(request,'Failed to store the Data.')
    return redirect('t_list')

# telicaller edit
@login_required(login_url="login")
def t_edit(request,id):
    try:
        manager_list = get_object_or_404(TelliCaller,id=id)
        if request.method == 'POST':
            update = Tellicaller_data(request.POST ,instance=manager_list)
            if update.is_valid():
                update.save()
                messages.success(request,'Data Updated Successfully!')
                return redirect('t_list')
        update=Tellicaller_data(instance=manager_list)
        return render(request,'Store Master/tel_edit.html' ,{'update':update})
    except:
        messages.error(request,'Failed to Update the Data.')
    return redirect('t_list')

# telicaller delete
@login_required(login_url="login")
def t_delete(request,tel_name):
    try:
        telli =get_object_or_404(TelliCaller,id=id)
        telli.delete()
    except:
        messages.error(request,'Failed to Delete the Data.')
    finally:
        messages.success(request,'Data Deleted Successfully!')
    return redirect('t_list')


# sample
@login_required(login_url="login")
def viewpage(request):
    return render(request,'Incentive/viewpage.html')

@login_required(login_url="login")
def rgallary(request):
    return render(request,'Report/report_gallary.html')
