from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.SignupPage,name='signup'),
    path('',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),

]