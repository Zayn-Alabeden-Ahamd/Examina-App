from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Teacher , Question , Answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )

    class Meta:
        model = Teacher
        fields = ['id', 'user', 'user_id', 'age', 'star', 'permissions', 'active' ]        


class AnswerSerializer(serializers.ModelSerializer) :
    question=serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())      

    class Meta:
        model=Answer
        fields='__all__'  

class QuestionSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=Teacher.objects.all())
    answers=AnswerSerializer(many=True,read_only=True)
    class Meta:
        model = Question
        fields = '__all__'      

