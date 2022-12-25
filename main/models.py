from django.db import models

class User(models.Model):
    surname=models.CharField('surname',max_length=20)
    name = models.CharField('name',max_length=20)
    about = models.TextField('about')
    login = models.CharField('login',max_length=20)
    password = models.CharField('password',max_length=20)
    calculations=models.IntegerField('calculations',default=0)

    def __str__(self):
        return self.surname +" " + self.name

class Post(models.Model):
    image=models.ImageField(null=True,blank=True,upload_to="images/")

class Results(models.Model):
    userid=models.CharField('userid',max_length=200,default='')
    emotion=models.CharField('emotion',max_length=20)
    imagename = models.CharField('imagename', max_length=200)
