from django.shortcuts import render,HttpResponse,redirect
from .models import Task
# Create your views here.

def index(request):
    tasks=Task.objects.all()
    context={
        'tasks':tasks
    }
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def create_task(request):
    if request.method == 'POST' :
        title= request.POST.get('title')
        description= request.POST.get('description')
        
        if title == '' and description == '':
            context ={
                'error': 'Both fields are required'
            }
            return render(request,'create_task.html',context)

        task=Task.objects.create(title=title,description=description)
        return redirect("/")
    
    return render(request,'create_task.html')
 
def update_task(request,pk):
    task=Task.objects.get(pk=pk)
    context={
        'task':task
    }
    
    if request.method == "POST":
        title= request.POST.get('title')
        description= request.POST.get('description')
        
        if title == '' and description == '':
            context ={
                'error': 'Both fields are required'
            }
            return render(request,'create_task.html',context)
        task.title=title
        task.description=description
        task.status=False
        task.save()
        return redirect("/")      
    return render(request,'update_task.html',context)


def delete_task(request,pk):
    task=Task.objects.get(pk=pk)
    task.delete()
    return redirect('/')


def mark_as_completed(request,pk):
    task=Task.objects.get(pk=pk)
    task.status=True
    task.save()
    return redirect('/')



# def mark_as_uncompleted(request,pk):
#     task=Task.objects.get(pk=pk)
#     task.status=True
#     task.delete()
#     return redirect('/')
