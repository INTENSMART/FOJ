"""pythonProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from django.urls import include, path
from .import views
from .forms import connexionForm
from django.contrib.auth import views as password_view

urlpatterns = [
    path('',views.home,name='index'),
    path('administrateurSignUp',views.inscriptionPage,name='administrateurSignUp'),
    #path('administrateurLogin',views.connexionPage,name='administrateurLogin'),
    path('administrateurLogin',auth_view.LoginView.as_view(template_name='connexion/login.html', redirect_authenticated_user=False,authentication_form=connexionForm),name='administrateurLogin'),
    path('etablissement',views.newEtablissement,name='etablissement'),
    path('dashboardAdmin', views.dashboardAdmin, name='dashboardAdmin'),
    #path('reset_Password', password_view.PasswordResetView.as_view(template_name='motDePasse/forgot-password.html'), name='reset_Password'),
    path('reset_Password', views.password_reset_request, name='reset_Password'),
    path('password_reset_done', password_view.PasswordResetDoneView.as_view(template_name='motDePasse/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', password_view.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete', password_view.PasswordResetCompleteView.as_view(template_name='motDePasse/password_reset_complete.html'), name='password_reset_complete'),
    path('confirmEmail', views.confirmEmail, name='confirmEmail'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
]
