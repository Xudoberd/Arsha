from django.db import models
class Type(models.Model):
    nomi = models.CharField(max_length=500)
    def __str__(self):
        return self.nomi
# Create your models here.
class Portfolio(models.Model):
    nomi = models.CharField(max_length=500)
    comp_name = models.CharField(max_length=500)
    tur = models.ForeignKey(Type,on_delete=models.CASCADE)
    url = models.CharField(max_length=651,null=True,blank=True)
    date = models.DateTimeField()
    text = models.TextField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media',)
    rasm3 = models.ImageField(upload_to='media',)

class Jamoa(models.Model):
    name = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='media',null=True,blank=True)
    request = models.CharField(max_length=100)
    text = models.TextField()
    tw = models.CharField(max_length=200,null=True,blank=True)
    fb = models.CharField(max_length=200,null=True,blank=True)
    insta = models.CharField(max_length=200,null=True,blank=True)
    inn = models.CharField(max_length=200,null=True,blank=True)

class Servis(models.Model):
    photo = models.ImageField(upload_to='media')
    name = models.CharField(max_length=90)
    text = models.CharField(max_length=500)

class Murojat(models.Model):
    ism = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)
    sub = models.CharField(max_length=30)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
