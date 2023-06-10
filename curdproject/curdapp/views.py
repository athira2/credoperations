
from django.shortcuts import render, get_object_or_404,redirect

from .models import Task


# Create your views here.
def add(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        slno=request.POST.get('slno','')
        Item_name=request.POST.get('Item_name','')
        desc = request.POST.get('desc', '')
        task=Task(slno=slno,Item_name=Item_name,desc=desc)
        task.save()

    return render(request,'home.html',{'task1':task1})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method =='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',)

def update(request,task_id1):
    task=get_object_or_404(Task,id=task_id1)
    if request.method=='POST':
        task.slno=request.POST.get('slno')
        task.item_name=request.POST.get('Item_name')
        task.desc=request.POST.get('desc')
        
        task.save()
        return redirect('/')
        # task=task.objects.all()
    return render(request,'update.html',{'task':task}) 