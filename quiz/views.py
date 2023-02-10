from django.shortcuts import render
from .models import QuesModel
from django.http import HttpResponse
from random import shuffle


# Create your views here.

def base(request):
    return render(request, 'quiz/startquiz.html')

def startquiz(request):
    return render(request, 'quiz/startquiz.html')

def questions_list(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.objects.all()
        score = 0
        total = 0
        for question in questions:
            total += 1
            print(request.POST.get(question.question))
            print(question.ans)
            print()
            if question.ans == request.POST.get(question.question):
                score += 1
        context = { 
            'score': score,
            'total': total
        }
        return render(request, 'quiz/results.html', context)
    else:
        questions = QuesModel.objects.all().order_by('?')
        return render(request, 'quiz/questions_list.html', {'questions' : questions})

def results(request):
    return render(request, 'quiz/results.html')