from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return 'Question: %s' % self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return 'the choice \"%s\" for the question \"%s\"' % (self.choice_text,self.question.question_text)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=10,choices=[('band','Band'),('athletics','Athletics'),('debate','Debate'),('art','Art')])
    answeredQuestions = models.ManyToManyField(Question)

    def __str__(self):
        return '%s, in the category %s' % (self.user.username,self.category)
