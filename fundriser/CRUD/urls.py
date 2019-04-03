from django.conf.urls import url  
from django.contrib import admin  
from CRUD_FBVs import views  
   
app_name = 'CRUD_FBVs'  
   
urlpatterns = [  
     url('admin/', admin.site.urls),  
     url(r'^$', views.movies_list, name='movies_list'),
    url(r'^new$', views.movies_create, name='movies_new'),
    url('^accounts/', admin.site.urls),
     
 ]  
