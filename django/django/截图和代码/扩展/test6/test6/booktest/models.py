from django.db import models
from tinymce.models import HTMLField

class AreaInfo(models.Model):
    title=models.CharField(max_length=20)
    parea=models.ForeignKey('self',null=True,blank=True)

class Test1(models.Model):
    content=HTMLField()


