from django.db import models
from django.contrib.auth.models import User


# Create your models here.
from django.db.models import constants


#class modelAdministrateur(models.Model):
  #  user=models.OneToOneField(User,on_delete=models.CASCADE,default=User)
  #  confirmPassword = models.CharField(max_length=200, null=True, blank=False)
   # created_at = models.DateField(auto_now_add=True)


  #  def __str__(self):
    #    return self.username


class modelEtablissement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=False, null=False)
    nomEtablissement = models.CharField(max_length=200, null=True, blank=False)
    telephone = models.IntegerField( null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=False)
    ville = models.CharField(max_length=200, null=True, blank=False)
    pays = models.CharField(max_length=200, null=True, blank=False)
    created_etablissement_at=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.nomEtablissement
