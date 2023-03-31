from django.urls import path
from quiz.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('questions_list', QuestionsList.as_view(), name='questions_list'),
    path('startquiz', StartQuiz.as_view(), name='startquiz'),
    path('results', Results.as_view(), name='results')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
