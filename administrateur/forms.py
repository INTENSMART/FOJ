from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from .models import  modelEtablissement



class administrateurForm(UserCreationForm):
    first_name = forms.CharField(help_text="Nom", widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user'}))
    last_name = forms.CharField(help_text="Prenom", widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user'}))
    username = forms.CharField(help_text="Nom d'utilisateur", widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user'}))
    email = forms.CharField(help_text="Adresse mail", widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-user'}))
    password1 = forms.CharField(help_text="Mot de passe", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user'}))
    password2 = forms.CharField(help_text="Confirmer le mot de passe", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user'}))
    class Meta:
       model=User
       fields=['first_name','last_name','username','email','password1','password2']

class connexionForm(AuthenticationForm):
    username = forms.CharField(help_text="Nom d'utilisateur", widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user'}))
    password = forms.CharField(help_text="Mot de passe", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-user'}))


class etablissementForm(forms.ModelForm):
    nomEtablissement = forms.CharField(help_text="Nom", widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user'}))
    telephone = forms.IntegerField(help_text="Numero de telephone", widget=forms.NumberInput(
        attrs={'class': 'form-control form-control-user'}))
    email = forms.CharField(help_text="Adresse mail", widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-user'}))
    ville = forms.CharField(help_text="ville", widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user'}))
    pays = forms.CharField(help_text="Pays", widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user'}))
    created_etablissement_at = forms.CharField(help_text="Pays", widget=forms.TextInput(
        attrs={'class': 'form-control form-control-user'}))
    class Meta:
        model=modelEtablissement
        fields='__all__'



class forgotPasswordForm(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control form-control-user'}))

