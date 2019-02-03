# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Records(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    residence = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    education = models.CharField(max_length=150, null=True)
    occupation = models.CharField(max_length=150, null=True)
    marital_status = models.CharField(max_length=50, null=True)
    bio = models.TextField()
    recorded_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.id
    class Meta:
        verbose_name_plural = "Records"              #so that in database table name is "Records" as by default django add s to model name so if we don't use verbose_name_plural then table name "Recordss" will be formed
class Files(models.Model):
    patient_no = models.CharField(max_length=10,null=True)
    prescription_no = models.CharField(max_length=10,null=True)
    pfile = models.TextField()
    date = models.DateTimeField(default=datetime.now,blank=True)
