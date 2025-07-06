from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.SmallIntegerField()
    star = models.BooleanField()
    permissions = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Question(models.Model):

    questioncode=models.CharField(primary_key=True, max_length=100)
    questionName=models.CharField(max_length=200)
    questionRate= models.CharField(max_length=100)
    questionText=models.CharField(max_length=255)
    questionGrade=models.CharField(max_length=100)

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.questionName

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    
