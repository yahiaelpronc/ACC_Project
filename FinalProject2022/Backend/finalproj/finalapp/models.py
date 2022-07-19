from django.db import models

# Create your models here.


class Myuser(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=30, null=False)
    firstname = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True, max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=20, null=True)
    b_date = models.DateField(max_length=20, null=True)
    active_status = models.BooleanField(default=False)
    face_link = models.URLField(null=True)
    active_link = models.URLField(null=True)
    profile_pic = models.ImageField(null=True)


class Vet(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=30, null=False)
    firstname = models.CharField(max_length=30, null=False)
    lastname = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True, max_length=30, null=False)
    password = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=True)
    mobile = models.CharField(max_length=20, null=True)
    b_date = models.DateField(max_length=20, null=True)
    active_status = models.BooleanField(default=False)
    face_link = models.URLField(null=True)
    active_link = models.URLField(null=True)
    profile_pic = models.ImageField(null=True)
    address = models.CharField(max_length=40, null=False)
    specialization = models.CharField(max_length=100, null=False, choices=(('poultry', 'poultry'), ('equine', 'equine'), ('ruminant', 'ruminant'),
                                                                           ('fishes and aquatics',
                                                                            'fishes and aquatics'),
                                                                           ('obstetrics and gynecology', 'obstetrics and gynecology')))
