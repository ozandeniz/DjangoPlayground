from django.http import HttpResponse
from poll.models import Question
from django.template import loader
from django.shortcuts import render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5] #Last 5 poll questions
    template = loader.get_template('poll/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'poll/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)