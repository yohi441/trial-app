from sqlite3 import DatabaseError
from django.shortcuts import render, redirect
import recipe
from recipe.forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from recipe.models import Recipe




class IndexView(View):

    def get(self, request):
        recipes = Recipe.objects.all()
  
        context = {
            'recipes': recipes
        }
        return render(request, 'index.html', context)


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


class DashboardView(LoginRequiredMixin, ListView):

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)

    model = Recipe
    template_name = "dashboard.html"
    paginate_by = 10
    context_object_name = 'recipes'
    ordering = ['-created']


class DetailView(View):


    def get(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        context = {
            'recipe': recipe
        }
        return render(request, 'detail_view.html', context)

