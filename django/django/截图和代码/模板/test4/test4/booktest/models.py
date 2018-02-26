from django.db import models

class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField()
    bcommet=models.IntegerField()
    isDelete=models.BooleanField()
    class Meta():
        db_table='bookinfo'

class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField()
    hcontent=models.CharField(max_length=1000)
    isDelete=models.BooleanField()
    book=models.ForeignKey('BookInfo')
    def showname(self):
        return self.hname

