from django.db import models

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True,max_length=6,null=False)
    email = models.EmailField(null=False)
    password = models.CharField(null=False)
    
