from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=200,null=True)
    mname = models.CharField(max_length=200,null=True)
    lname = models.CharField(max_length=200,null=True)
    ph = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    dob = models.CharField(max_length=200,null=True)
    occupation = models.CharField(max_length=200,null=True)
    nam = models.CharField(max_length=200,null=True)
    relation = models.CharField(max_length=200,null=True)
    raddress = models.CharField(max_length=200,null=True)
    paddress = models.CharField(max_length=200,null=True)
    adhar = models.CharField(max_length=200,null=True)
    p_name = models.CharField(max_length=100 ,null=True)

    def __str__(self):
        return str(self.id)
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    df = models.CharField(null=True, max_length=50)
    dt = models.DateField()
    fname = models.CharField(max_length=200,null=True)
    mname = models.CharField(max_length=200,null=True)
    lname = models.CharField(max_length=200,null=True)
    ph = models.CharField(max_length=200,null=True)
    mail = models.CharField(max_length=200,null=True)
    dob = models.CharField(max_length=200,null=True)
    occupation = models.CharField(max_length=200,null=True)
    nam = models.CharField(max_length=200,null=True)
    relation = models.CharField(max_length=200,null=True)
    raddress = models.CharField(max_length=200,null=True)
    paddress = models.CharField(max_length=200,null=True)
    adhar = models.CharField(max_length=200,null=True)
    exname = models.CharField(max_length=200,null=True)
    maname = models.CharField(max_length=200,null=True)
    tname = models.CharField(max_length=200,null=True)
    p_mode = models.CharField(max_length=200,null=True)
    remark = models.CharField(max_length=200,null=True)
    layout = models.CharField(max_length=200,null=True)
    nxt_dt = models.CharField(max_length=200,null=True)
    p_name =models.CharField(max_length=50,null=True)
    flt =models.CharField(max_length=50,null=True)
    sqft =models.CharField(max_length=50,null=True)
    rate =models.CharField(max_length=50,null=True)
    tamount=models.CharField(max_length=50,null=True)
    book_amt =models.CharField(max_length=50,null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        billing_master.objects.update_or_create(
            fname=self.fname,
            p_name = self.p_name,
            rate = self.rate,
            book_amt = self.book_amt,
            tamount = self.tamount,
            nxt_dt = self.nxt_dt,
            ph = self.ph,
            bill_no = self.id,
            flt = self.flt,
            dt = self.dt,
            balance=int(self.tamount)- int(self.book_amt),
            status='',
            del_status='',
        )

    def __str__(self):
        return str(self.id)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dt = models.DateField()
    fname = models.CharField(null=True , max_length=50)
    p_name = models.CharField(null=True , max_length=50)
    flt = models.CharField(null=True , max_length=50)
    bill_no = models.CharField(null=True , max_length=50)
    ph = models.CharField(null=True , max_length=50)
    executive_name = models.CharField(null=True , max_length=50)
    manager_name = models.CharField(null=True , max_length=50)
    tel_name = models.CharField(null=True , max_length=50)
    p_mode = models.CharField(null=True , max_length=50)
    paddress = models.CharField(null=True , max_length=50)
    book_amt = models.CharField(null=True , max_length=50)
    nxt_dt = models.CharField(null=True , max_length=50)
    status = models.CharField(default="Pending" , max_length=50)
    rate =models.CharField(max_length=50,null=True)
    tamount=models.CharField(max_length=50,null=True)
    def __str__(self):
        return str(self.id)
    
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(null=True, max_length=50)
    flt = models.CharField(null=True, max_length=50)
    def __str__(self):
        return str(self.id)
    
class Executive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    executive_name =models.CharField(null=True, max_length=50)
    phone_no =models.CharField(null=True, max_length=50)
    address =models.CharField(null=True, max_length=50)
    def __str__(self):
        return str(self.id)
    

class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manager_name =models.CharField(null=True, max_length=50)
    phone_no =models.CharField(null=True, max_length=50)
    address =models.CharField(null=True, max_length=50)
    def __str__(self):
        return str(self.id)
    
class TelliCaller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tel_name =models.CharField(null=True, max_length=50)
    phone_no =models.CharField(null=True, max_length=50)
    address =models.CharField(null=True, max_length=50)
    def __str__(self):
        return str(self.id)
    
class Incntive_executive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(null=True, max_length=50)
    ex_name = models.CharField(null=True, max_length=50)
    remark = models.CharField(null=True, max_length=50)
    amount = models.CharField(null=True, max_length=50)
    def __str__(self):
        return str(self.id)
    
class Manager_executive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(null=True,max_length=50)
    manager_name = models.CharField(null=True,max_length=50)
    remark = models.CharField(null=True,max_length=50)
    amount = models.CharField(null=True,max_length=50)
    def __str__(self):
        return str(self.id)
    
class Tellicaller_executive(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(null=True,max_length=50)
    tell_name = models.CharField(null=True,max_length=50)
    address = models.CharField(null=True,max_length=50)
    amount = models.CharField(null=True,max_length=50)
    def __str__(self):
        return str(self.id)
        
class billing_master(models.Model):
    fname   = models.CharField(null=True,max_length=50)
    p_name  = models.CharField(null=True,max_length=50)
    rate    = models.CharField(null=True,max_length=50)
    book_amt= models.CharField(null=True,max_length=50)
    tamount = models.CharField(null=True,max_length=50)
    balance = models.CharField(null=True,max_length=50,default=0)
    nxt_dt  = models.CharField(null=True,max_length=50)
    status  = models.CharField(null=True,max_length=50,default="None")
    ph  = models.CharField(null=True,max_length=50)
    bill_no = models.CharField(null=True,max_length=50)
    flt = models.CharField(null=True,max_length=50)
    del_status  = models.CharField(null=True,max_length=50,default="None")
    dt  = models.CharField(null=True,max_length=50)
    def __str__(self):
        return str(self.id)