from django.db import models

# Create your models here.
class Hospital(models.Model):
    id=models.AutoField(primary_key=True)
    hospital_name=models.CharField(max_length=255, unique=True)
    hospital_address=models.CharField(max_length=255, null=True, blank=True)

class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    doctor_name=models.CharField(max_length=255)
    specialization=models.CharField(max_length=255)
    years_of_experience=models.PositiveIntegerField()
    hospital_id=models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='Doc')

class Patient(models.Model):
    id=models.AutoField(primary_key=True)
    patient_name=models.CharField(max_length=255)
    age=models.PositiveIntegerField()
    ailment=models.CharField(max_length=255, null=True, blank=True)
    admitted_doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient')
    