# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Records(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254,null=True)
    sex = models.CharField(max_length=11,null=False)
    dob = models.DateField(auto_now=False,auto_now_add=False)
    height_in_inches = models.IntegerField()
    weight_in_kg = models.IntegerField()
    phone = models.CharField(max_length=10,null=False)
    marital_status = models.CharField(max_length=50, null=False)
    residence = models.CharField(max_length=200, null=False)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=50,null=False)
    country = models.CharField(max_length=50, null=False)
    emergency_contact_first_name = models.CharField(max_length=50)
    emergency_contact_last_name = models.CharField(max_length=50, null=True)
    emergency_contact_relationship = models.CharField(max_length=30,null=False)
    emergency_contact_phone_no = models.BigIntegerField()
    taking_any_medication_currently = models.CharField(max_length=3,null=False)
    medication_if_yes = models.TextField(max_length=300,null=True)
    recorded_created_at = models.DateTimeField(default=datetime.now, blank=True)
    # education = models.CharField(max_length=150, null=True)
    # occupation = models.CharField(max_length=150, null=True)
    # marital_status = models.CharField(max_length=50, null=True)
    # bio = models.TextField()

    def __str__(self):
        return self.id
    class Meta:
        verbose_name_plural = "Records"              #so that in database table name is "Records" as by default django add s to model name so if we don't use verbose_name_plural then table name "Recordss" will be formed
class Files(models.Model):
    patient_no = models.CharField(max_length=10,null=True)
    prescription_no = models.CharField(max_length=10,null=True)
    pfile = models.TextField()
    date = models.DateTimeField(default=datetime.now,blank=True)
