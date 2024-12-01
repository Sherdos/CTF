from django.urls import path
from users.views import LoginUserView, logout_user
urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]