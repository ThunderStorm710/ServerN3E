from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('contacts/', views.ContactsPage, name='contacts'),
    path('about/', views.AboutPage, name='about'),
    path('logout/', views.LogoutPage, name='logout'),
    path('door/', views.OpenDoor, name='openDoor'),
    path('accounts/', include("allauth.urls")),
]
