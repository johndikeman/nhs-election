from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Question, Choice
import json

@login_required
def index(request):
    template = loader.get_template('polls/index.html')
    questions = []
    for question in Question.objects.order_by('-pub_date'):
        if question not in request.user.student.answeredQuestions.all() and (question.spec == 'any' or question.spec == request.user.student.category):
            questions.append(question)
    context = {'questions':questions}
    return render(request,'polls/index.html',context)

@login_required
def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    if request.user.is_authenticated():
        if question not in request.user.student.answeredQuestions.all():
            try:
                selected_choice = question.choice_set.get(pk=request.POST['choice'])
            except (KeyError, Choice.DoesNotExist):
                # Redisplay the question voting form.
                return render(request, 'polls/detail.html', {
                    'question': question,
                    'error_message': "You didn't select a choice.",
                })
            selected_choice.votes += 1
            selected_choice.save()
            request.user.student.answeredQuestions.add(question)
            request.user.student.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))

@login_required
def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question,'user':request.user})

@login_required
def results(request,id):
    labels = []
    data = []
    question = get_object_or_404(Question,pk=id)
    for a in question.choice_set.all():
        labels.append(a.choice_text)
        data.append(a.votes)
    fin = {
        'labels':labels,
        'datasets':
            [
                {
                    'label': 'a results graph',
                    'fillColor': "rgba(220,220,220,0.2)",
                    'strokeColor': "rgba(220,220,220,1)",
                    'pointColor': "rgba(220,220,220,1)",
                    'pointStrokeColor': "#fff",
                    'pointHighlightFill': "#fff",
                    'pointHighlightStroke': "rgba(220,220,220,1)",
                    'data': data
                }
            ],

    }

    return render(request,'polls/results.html',{'graph_data':json.dumps(fin)})

def results_api(request,id):
    return HttpResponse('ass')

def login_page(request):
    if request.method == 'POST':
        username, password = request.POST['username'],request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'polls/login.html',context={'error':'that username/password combo didn\'t work, boss.'})

    if request.method == 'GET':
        return render(request,'polls/login.html',context={'error':None})


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def data_page(request):
    pass
