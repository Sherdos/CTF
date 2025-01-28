from django.urls import path
from tasks.views import index, show_ctf, check_answer, progress_ctf
from tasks.consumers import CtfConsumer
urlpatterns = [
    path('', index, name='index'),
    path('ctf/<int:id>', show_ctf, name='show_ctf'),
    path('check/answer/<int:id>', check_answer, name='check_answer'),
    path('progress/ctf/<int:id>', progress_ctf, name='progress_ctf'),
]