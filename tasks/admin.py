from django.contrib import admin
from tasks.models import User, Answer, Task, Ctf, Machine

admin.site.register(User)
admin.site.register(Answer)
admin.site.register(Task)
admin.site.register(Ctf)
admin.site.register(Machine)

# Register your models here.
