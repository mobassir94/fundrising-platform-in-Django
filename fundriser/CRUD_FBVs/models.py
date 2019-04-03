from django.db import models  
from django.urls import reverse  
from django.contrib.auth.models import User  
  
  
class CRUD(models.Model):  
 
    
   fund_required = models.CharField(max_length=200)  
   fund_given = models.CharField(max_length=200)  
  
   def __unicode__(self):  
     return self.title  
  
   def get_absolute_url(self):  
     return reverse('CRUD_FBVs:movies_edit', kwargs={'pk': self.pk})  
