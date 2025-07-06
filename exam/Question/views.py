from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Teacher, Question 
from .serializers import TeacherSerializer, QuestionSerializer 



class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Question.objects.filter(teacher=self.request.user.teacher)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user.teacher)



