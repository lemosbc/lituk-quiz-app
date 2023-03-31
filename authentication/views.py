from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('startquiz')


class RegisterPage(FormView):
    template_name = 'authentication/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('startquiz')

    def form_valid(self, form):
        user = form.save()
        if user is not None: # If user was successfully created
            login(self.request, user) # Login the user that was just created
        return super(RegisterPage, self).form_valid(form)

    # Redirects authencitade users if they try to access
    # the 'register' page
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('startquiz')
        return super(RegisterPage, self).get(*args, **kwargs)

