from django.urls import path
from quiz.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', base, name='base'),
    path('questions_list', questions_list, name='questions_list'),
    path('startquiz', startquiz, name='startquiz'),
    path('results', results, name='results')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
