from django.shortcuts import render, redirect
from tasks.models import Ctf, Task, Answer
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

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
    task_ids = []
    if request.user.is_authenticated:
        task_ids = request.user.answers.values_list('task_id', flat=True)
    
    context = {
        'ctf':ctf,
        'task_ids':task_ids
    }
    return render(request, template_name, context)

def check_answer(request, id):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        task = get_object_or_404(Task, id=id)
        ctf = task.ctf

        if flag == task.flag:
            if ctf.ctf_type == Ctf.SINGLE_PLAYER:
                if not Answer.objects.filter(user=request.user, task=task).exists():
                    Answer.objects.create(user=request.user, task=task)
                    messages.success(request, "Correct flag! Task solved.")
            elif ctf.ctf_type == Ctf.COMPETITIVE:
                if not Answer.objects.filter(task=task).exists():
                    Answer.objects.create(user=request.user, task=task)
                    messages.success(request, "Correct flag! Task solved.")
        else:
            messages.error(request, "Incorrect flag. Try again.")

    return redirect('show_ctf', task.ctf_id)


def progress_ctf(request, id):
    template_name = 'tasks/progress_ctf.html'
    ctf = Ctf.objects.get(id=id)
    answers = Answer.objects.filter(task__ctf=ctf).select_related('user', 'task')
    
    context = {
        'ctf': ctf,
        'task_ids': [],
        'answers': answers,
    }
    return render(request, template_name, context)





# def show_leaderboards(request, id):
#     template_name = 'tasks/show_leaderboards.html'
#     ctf = Ctf.objects.get(id=id)
    
#     context = {
#         'ctf':ctf,
#     }
#     return render(request, template_name, context)