from pyexpat import model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class Member(models.Model):

    class Meta:
        pass

    first_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    address = models.TextField(max_length=500)
    phone_no = PhoneNumberField()
    emai_address = models.EmailField()

    #Next Of Kin
    nok_first_name = models.CharField(max_length=255 )
    nok_surname = models.CharField(max_length=255)
    nok_last_name= models.CharField(max_length=255)
    nok_address = models.TextField(max_length=500)
    nok_phone_no = PhoneNumberField()
    nok_relationship = models.CharField(max_length=25)
    nok_emai_address = models.EmailField()


    def __str__(self):
        return self.name
    


    
