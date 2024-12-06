from django.contrib import admin
from tasks.models import Answer, Task, Ctf, Machine, Setting

admin.site.register(Answer)
admin.site.register(Task)
admin.site.register(Ctf)
admin.site.register(Machine)
admin.site.register(Setting)

# Register your models here.
