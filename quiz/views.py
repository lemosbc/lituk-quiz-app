from django.shortcuts import render
from .models import QuesModel, UserResults
from django.http import HttpResponse

from django.views.generic.edit import CreateView



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
        questions = QuesModel.objects.all().order_by('?')[:24] # Randomizes questions in database and selects the first 24
        return render(request, 'quiz/questions_list.html', {'questions' : questions})

def results(request):
    return render(request, 'quiz/results.html')


class SubmitResult(CreateView):
    model = UserResults
    result = questions_list
    ##def get_result(request):
    ##    if request.method == 'POST'