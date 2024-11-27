from django.shortcuts import render, redirect
from tasks.models import Ctf, Task, Answer
# Create your views here.



def index(request):
    template_name = 'tasks/index.html'
    ctfs = Ctf.objects.all()
    context = {
        'ctfs':ctfs,
    }
    return render(request, template_name, context)

def show_ctf(request, id):
    template_name = 'tasks/show_ctf.html'
    ctf = Ctf.objects.get(id=id)
    task_ids = request.user.answers.values_list('task_id', flat=True)
    context = {
        'ctf':ctf,
        'task_ids':task_ids
    }
    return render(request, template_name, context)

def check_answer(request, id):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        task = Task.objects.get(id=id)
        if flag == task.flag:
            Answer.objects.create(user = request.user, task = task)
        
    return redirect('show_ctf', task.ctf_id)