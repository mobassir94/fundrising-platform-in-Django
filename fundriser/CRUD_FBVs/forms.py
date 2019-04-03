from django import forms  
from .models import CRUD  
   
   
class MoviesForm(forms.ModelForm):
     class Meta:
          model = CRUD
          fields = ['fund_required', 'fund_given'] 
   
       
         
          
