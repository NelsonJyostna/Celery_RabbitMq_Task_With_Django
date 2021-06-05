from django.shortcuts import render
from rest_framework.response import  Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.views import APIView
from .task import *




# Create your views here.
class StudentAPI(APIView):
    def get(self, request, pk=None):
        id=pk
        if id is not None:
            std=Student.objects.get(id=id)
            serializer=StudentSerializer(std)
            return Response(serializer.data)
        std=Student.objects.all()
        serializer=StudentSerializer(std, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            sleepy.delay(10)
            return Response({'msg':'User Register'}, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        id = pk
        std = Student.objects.get(pk=id)
        serializer = StudentSerializer(std, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Completed'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        id = pk
        std = Student.objects.get(pk=id)
        serializer = StudentSerializer(std, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            sleepy.delay(10)
            return Response({'msg': 'Partial data Completed'})
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        id = pk
        std = Student.objects.get(pk=id)
        std.delete()
        return Response({'msg': 'Data Deleted'})
