from django.db import models

# Create your models here.
class Msg(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=200,null=True)
    phone= models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name

    
