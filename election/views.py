from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Question, Choice
# Create your views here.

@login_required
def index(request):
    template = loader.get_template('polls/index.html')

    context = {'questions':Question.objects.order_by('-pub_date')[:5]}
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
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('index'))

@login_required
def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question,'user':request.user})

def logon_page(request):
    username, password = request.POST['username'],request.POST['password']
    user = authenticate(username=username,password=password)
    if user is not None:
        print user.student
        login(request,user)

    return HttpResponseRedirect(reverse('index'))

def login_page(request):
    return render(request,'polls/login.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def data_page(request):
    pass
