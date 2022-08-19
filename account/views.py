from django.shortcuts import render, redirect
from account.forms import LoginForm, RegisterForm
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View





class SigninView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        form = LoginForm()
        context = {
            'form' : form
        }
        return render(request, 'signin.html', {'form': form})

    def post(self, request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('index'))

        context = {
            'form': form,
        }

        return render(request, 'signin.html', {'form': form})
    

class SignoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect(reverse('signin'))

class SignupView(View):

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        
        context = {
            'form': form,
        }
        return render(request, 'signup.html', context)

    def get(self, request):
        form = RegisterForm()
        if request.user.is_authenticated:
            return redirect('index')

        context = {
            'form': form,
        }
        return render(request, 'signup.html', context)

class SignupSuccessView(View):

    def get(self, request):
        
        return render(request, 'signup_success.html', {})

