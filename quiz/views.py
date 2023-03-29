from django.shortcuts import render
from .models import QuesModel, UserResults
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView


# Create your views here.

def home(request):
    return render(request, 'quiz/home.html')

def startquiz(request):
    return render(request, 'quiz/startquiz.html')

class QuestionsList(View):
    form_class = QuesModel
    
   
    def get(self, request, *args, **kwargs):
        questions = QuesModel.objects.all().order_by('?')[:24] # Randomizes questions in database and selects the first 24
        return render(request, 'quiz/questions_list.html', {'questions' : questions})
    
    def post(self, request, *args, **kwargs):
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
        
def results(request):
    return render(request, 'quiz/results.html')


#class SubmitResult(CreateView):
#    model = UserResults
#    result = QuestionsList
#    def get_result(request):
#    if request.method == 'POST'