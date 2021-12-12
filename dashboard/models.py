from django.db import models
from django.contrib.auth.models import  User
#from taggit.managers import TaggableManager

# Create your models here.
class Notes(models.Model):
 user=models.ForeignKey(User, on_delete=models.CASCADE)
 title = models.CharField(max_length=45)
 description = models.CharField(max_length=250) 
 def __str__(self):
     return self.title
 
 class Meta:
   verbose_name = "notes"
   verbose_name_plural ="notes"
                