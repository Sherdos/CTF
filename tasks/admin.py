from django.contrib import admin
from tasks.models import Answer, Task, Ctf, Machine

admin.site.register(Answer)
admin.site.register(Task)
admin.site.register(Ctf)
admin.site.register(Machine)

# Register your models here.
