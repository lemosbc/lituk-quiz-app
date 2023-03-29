from django.urls import path
from .views import RegisterPage


urlpatterns = [
    path('', RegisterPage.as_view(), name='register'),

]
