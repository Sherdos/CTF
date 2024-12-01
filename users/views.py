from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from users.forms import LoginUserForm
from django.contrib.auth import logout
# Create your views here.



class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'user/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')
