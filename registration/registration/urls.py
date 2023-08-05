from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('', views.LandingPage, name='landing'),
    #path('home/', views.HomePage, name='home'),
    path('home/', views.HomeDashboard, name='home'),
    #path('home/', TemplateView.as_view(template_name='dashboard/home.html'), name='home'),
    path('contacts/', views.ContactsPage, name='contacts'),
    path('about/', views.AboutPage, name='about'),
    path('logout/', views.LogoutPage, name='logout'),
    path('door/', views.OpenDoor, name='openDoor'),
    path('settings/', views.Settings, name='settings'),
    path('profile/', views.Profile, name='profile'),
    path('eletronica/', views.Eletronica, name='eletronica'),
    path('robotics/', views.Robotics, name='robotics'),
    path('accounts/', include("allauth.urls")),
]
