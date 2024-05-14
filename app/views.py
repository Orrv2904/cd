from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Tarea
# Create your views here.

# @login_required
def home(request):
    tareas = Tarea.objects.all()
    context = {
         "tareas": tareas,
     }
    return render(request, "index.html", context)


@login_required
def crear(request):
    if request.method == 'GET':
        form = TareaForm()
        context = {
            "form": form,
        }
        return render(request, 'crear.html', context)
    else:
        form2 = TareaForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('crear')
        else:
            return JsonResponse({'success': False, 'message': 'No se pudo guardar'})