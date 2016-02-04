from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils.timezone import now

cat = [('band','Band'),('athletics','Athletics'),('debate','Debate'),('art','Art')]

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    spec = models.CharField(max_length=25, choices=(cat+[('any','any')]),default='any')
    # this is the time in hours that the question will be active for
    time_limit = models.IntegerField(default=72)
    is_finished = models.BooleanField(default=False)
    winner = models.CharField(max_length=300,blank=True)

    def get_time_left(self):
        # returns a tuple in the form (days, hours)
        print now()
        if self.is_finished:
            return (0,0)
        tim = ((self.pub_date + timedelta(hours=self.time_limit)) - now())

        return (tim.days,tim.seconds)

    def __str__(self):
        return 'Question for %s: %s' % (self.spec,self.question_text)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return 'the choice \"%s\" for the question \"%s\"' % (self.choice_text,self.question.question_text)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=10,choices=cat)
    answeredQuestions = models.ManyToManyField(Question,blank=True)

    def can_vote_on(self,question):
        if question.is_finished:
            return False

        if question not in self.answeredQuestions.all():
            if (question.spec == 'any' or question.spec == self.category):
                return True
        return False

    def __str__(self):
        return '%s, in the category %s' % (self.user.username,self.category)
