from django.db import models


class Raw_data(models.Model):
        name      = models.CharField(default="", max_length=300)
        email     = models.EmailField(default="", max_length=246)
        mobileno  = models.PositiveIntegerField(default=0)
        address   = models.TextField()
        Photo     = models.ImageField(upload_to="profile/",max_length=500,blank=True,null=True,)
        password  = models.TextField(default="", max_length=200)
        Register_date = models.DateTimeField(auto_now=True, blank=True,null=True)
    
        def __str__(self):
            return self.name
    
    
class Cus_data(models.Model):
    raw = models.ForeignKey('Raw_data',on_delete=models.CASCADE,blank=True,null=True)
    cus_nm = models.CharField(default="",max_length=200)
    cus_em = models.EmailField(default="",max_length=200)
    cus_con = models.PositiveIntegerField(default=0)
    cus_add1 = models.TextField(default="")
    cus_regi_date = models.DateTimeField(auto_now_add=True,blank=True, null=True) 
    cus_photo = models.ImageField(upload_to="Cus_Photo/",default="",max_length=300,blank=True, null=True)
    cus_pass = models.CharField(default="",max_length=200)        

    def __str__(self):
        return self.cus_nm
    

class mg_data(models.Model):
    raw = models.ForeignKey('Raw_data',on_delete=models.CASCADE,blank=True,null=True)
    cus = models.ForeignKey('Cus_data',on_delete=models.CASCADE,blank=True,null=True)
    mg_em = models.EmailField(default="",max_length=200)
    mg_con = models.PositiveIntegerField(default=0)
    mg_mass = models.TextField(default="")
    mg_regi_date = models.DateTimeField(auto_now_add=True,blank=True, null=True) 
    mg_nm = models.CharField(default="",max_length=200)        

    def __str__(self):
        return self.mg_nm


class Company_Product(models.Model):
    comp = models.ForeignKey('Raw_data',on_delete=models.CASCADE,blank=True,null=True)
    pro_nm = models.CharField(default="",max_length=200)
    pro_pr = models.PositiveIntegerField(default=0)
    pro_qty = models.PositiveIntegerField(default=0)
    pro_img = models.ImageField(upload_to="ProductPic/",default="",max_length=300,blank=True, null=True)

    def __str__(self):
        return self.pro_nm

class Customer_orders(models.Model):
    comp = models.ForeignKey('Raw_data',on_delete=models.CASCADE,blank=True,null=True)
    cust = models.ForeignKey('Cus_data',on_delete=models.CASCADE,blank=True,null=True)
    prod = models.ForeignKey('Company_Product',on_delete=models.CASCADE,blank=True,null=True)
    tot_price = models.PositiveIntegerField(default=0)
    qty = models.PositiveIntegerField(default=0)
    order_date = models.DateTimeField(auto_now_add=True,blank=True, null=True) 
    status = models.CharField(default="Waiting",max_length=20)

    def __str__(self):
        return self.status