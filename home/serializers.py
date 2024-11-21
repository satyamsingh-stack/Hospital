from rest_framework import serializers
from .models import *

class HospitalSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Hospital
        fields='__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

class PatientSerailizer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'

