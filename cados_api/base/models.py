from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
class Advocate(models.Model):
    name = models.CharField(max_length=200)
    profile_pic = models.CharField(max_length=500, null=True, blank=True)
    company = models.ForeignKey(Company,on_delete=models.SET_NULL, blank=True, null=True)
    username = models.CharField(max_length=500, null=True, blank=True)
    bio = models.TextField(max_length=550, null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    

