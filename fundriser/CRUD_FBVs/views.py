from django.contrib.auth.decorators import login_required  
from django.shortcuts import render, get_object_or_404, redirect  
from .forms import MoviesForm  
from CRUD_FBVs.models import CRUD  
  
  
@login_required  
def movies_list(request):  
     if request.user.is_superuser:  
         movies = CRUD.objects.all()  
     else:  
         movies = Movies.objects.filter(user=request.user)  
     return render(request, 'movies_list.html', {  
         'object_list': movies  
     })  
  
  
@login_required  
def movies_create(request):  
     form = MoviesForm(request.POST or None)
    
   
     if form.is_valid():  
         movies = form.save(commit=False)  
         movies.user = request.user
         movies.save()
         return redirect('/')   
     return render(request, 'movies_form.html', {'form': form})  
  
  
@login_required  
def movies_update(request, pk):  
     if request.user.is_superuser:  
         movies = get_object_or_404(Movies, pk=pk)  
     else:  
         movies = get_object_or_404(Movies, pk=pk, user=request.user)  
     form = MoviesForm(request.POST or None, instance=movies)  
     if form.is_valid():  
         form.save()  
         return redirect('CRUD_FBVs:movies_list')  
     return render(request, 'movies_form.html', {'form': form})  
  
  
@login_required  
def movies_delete(request, pk):  
     if request.user.is_superuser:  
         movies = get_object_or_404(Movies, pk=pk)  
     else:  
         movies = get_object_or_404(Movies, pk=pk, user=request.user)  
     if request.method == 'POST':  
         movies.delete()  
         return redirect('CRUD_FBVs:movies_list')  
     return render(request, 'confirm_delete.html', {'object': movies})  
