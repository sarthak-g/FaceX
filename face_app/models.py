from django.db import models

# Create your models here.
class Record(models.Model):
    aadhar_no = models.IntegerField(primary_key = True)
class Files(models.Model):

    aadhar_no = models.IntegerField(max_length=12)
    date_of_visiting = models.CharField(max_length=11,null=True)
    symptoms = models.TextField(max_length=300,null=True)
    drugs = models.TextField(max_length=300,null=True)
    dosage = models.TextField(max_length=300,null=True)
    tests_to_be_done = models.TextField(max_length=300,null=True)
    date_for_revisit = models.CharField(max_length=11,null=True)
