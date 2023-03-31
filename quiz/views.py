from django.shortcuts import render
from .models import QuesModel, UserResults
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView


# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, 'quiz/home.html')
    
class StartQuiz(View):
    def get(self, request):
        return render(request, 'quiz/startquiz.html')

class QuestionsList(View):
    form_class = QuesModel
    score = 0
       
    def get(self, request, *args, **kwargs):
        questions = QuesModel.objects.all().order_by('?')[:24] # Randomizes questions in database and selects the first 24
        return render(request, 'quiz/questions_list.html', {'questions' : questions})
    
    def post(self, request, *args, **kwargs):
        attempt_score = QuestionsList.score
        questions = QuesModel.objects.all()
        for question in questions:
            print(request.POST.get(question.question))
            print(question.ans)
            print()
            if question.ans == request.POST.get(question.question):
                attempt_score += 1
        context = { 
            'attempt_score': attempt_score,
        }
        
        return render(request, 'quiz/results.html', context)
    
class SubmitResult(QuestionsList):
    form_class = UserResults
    

    def get(self, request, *args, **kwargs):
        return
    
    def post(self, request, questions_list, *args, **kwargs):
        score = questions_list.score
        user_results = UserResults(request.POST)
        user_results.user = request.user.username
        result = score
        user_results.result = result
        user_results.save()
        return
    
        
class Results(View):
    def get(self, request):
        return render(request, 'quiz/results.html')


