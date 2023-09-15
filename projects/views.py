from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.response import Response

class ProjectsAPI(APIView):

    def get(self, request):
        model = Project.objects.all()
        serializer = ProjectSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
