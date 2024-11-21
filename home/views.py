from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Operation1(APIView):
    def post(self,request):
        serializer=HospitalSerailizer(data=request.data)
        if(serializer.is_valid()):
            hospital_name=serializer.validated_data['hospital_name']
            if(Hospital.objects.filter(hospital_name=hospital_name).exists()):
                return Response("already existed", status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        hos=Hospital.objects.all()
        serializer=HospitalSerailizer(hos,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Operation2(APIView):
    def post(self,request):
        serializer=DoctorSerializer(data=request.data)
        if(serializer.is_valid()):
            hospital_id=request.data.get('hospital_id')
            if(Hospital.objects.filter(id=hospital_id).exists()):
                if(request.data.get('years_of_experience')>0):
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response({"Less age"},status=status.HTTP_400_BAD_REQUEST)
            return Response({"Data not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        doc=Doctor.objects.all()
        serializer=DoctorSerializer(doc,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Operation3(APIView):
    def post(self,request):
        serializer=PatientSerailizer(data=request.data)
        if(serializer.is_valid()):
            admitted_doctor=request.data.get('admitted_doctor')
            if(Doctor.objects.filter(id=admitted_doctor).exists()):
                if(request.data.get('age')>0 and request.data.get('age')<120):
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_201_CREATED)
                return Response({"Invalid age"},status=status.HTTP_400_BAD_REQUEST)
            return Response({"Data not found"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        pat=Patient.objects.all()
        serializer=PatientSerailizer(pat,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)