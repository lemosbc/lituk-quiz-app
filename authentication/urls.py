from django.urls import path
from .views import RegisterPage, CustomLoginView


urlpatterns = [
    path('', RegisterPage.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
