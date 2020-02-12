from django.db import models

# Create your models here.
class Essay1(models.Model):
    #id = models.AutoFieldMeta(primary_Key=True)
    name  =models.CharField(max_length=150)
    college = models.CharField(max_length=150)
    roll_no = models.CharField(max_length=150,primary_key=True)
    email = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    essay = models.CharField(max_length=10000)
    def __str__(self):
        return self.name