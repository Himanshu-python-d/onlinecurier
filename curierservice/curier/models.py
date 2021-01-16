from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.IntegerField()
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=45)


    def __str__(self):
        return self.user.username

class CurierList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=30)
    rcontact = models.IntegerField()
    pick_up_address = models.CharField(max_length=40)
    delivery_address = models.CharField(max_length=40)
    pweight = models.IntegerField()
    plength = models.IntegerField()
    pwidth = models.IntegerField()
    pheight = models.IntegerField()
    delivery_service = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username+" "+self.status
