from django.urls import path, re_path
from . import views

app_name = 'Users'

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),



]
