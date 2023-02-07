from django.db import models

# Create your models here.
class UserForm(models.Model):  
    firstname = models.CharField("Enter first name", max_length=50)  
    lastname  = models.CharField("Enter last name", max_length = 50)  
    date_of_birth = models.DateField("Enter date of birth",max_length=8) 
    file   = models.FileField() # for creating file input  
   
    class Meta:  
        
        managed = True
        db_table = 'user_profile'