from django.shortcuts import render, redirect
from .models import QuesModel, UserResults
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



class Home(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('startquiz')
        return render(request, 'quiz/home.html')

class StartQuiz(LoginRequiredMixin, View):
    login_url = 'auth/login/'
    def get(self, request):
        return render(request, 'quiz/startquiz.html')

class QuestionsList(LoginRequiredMixin,View):
    login_url = 'auth/login/'
    form_class = QuesModel
    score = 0
           
    def get(self, request, *args, **kwargs):
        questions = QuesModel.objects.all().order_by('?')[:24] # Randomizes questions in database and selects the first 24
        return render(request, 'quiz/questions_list.html', {'questions' : questions})
    
    def post(self, request, *args, **kwargs):
        attempt_score = QuestionsList.score
        questions = QuesModel.objects.all().order_by('?')[:24]
        for question in questions:
            print(request.POST.get(question.question))
            print(question.ans)
            if question.ans == request.POST.get(question.question):
                attempt_score += 1
        id = request.user
        user_results = UserResults(result = attempt_score, user_id = id )
        user_results.save()
        time_taken = 2700 - int(request.POST.get('timer'))
        seconds = time_taken % 60
        seconds_in_minutes = (time_taken - seconds) / 60
        minutes = int(seconds_in_minutes % 60)
        formatted_time = '{:02d}:{:02d}'.format(minutes, seconds)
        context = { 
            'attempt_score': attempt_score,
            'formatted_time' : formatted_time
        }
        print(context)
        
        return render(request, 'quiz/results.html', context)
    
