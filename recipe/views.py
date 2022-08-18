
from django.shortcuts import render, redirect
from recipe.forms import LoginForm, RegisterForm, RecipeForm, InlineFormSet
from django.contrib.auth import login, logout
from django.urls import reverse
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from recipe.models import Ingredient, Recipe
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory




class IndexView(ListView):
    model = Recipe
    template_name = "index.html"
    paginate_by = 6
    context_object_name = 'recipes'
    ordering = ['created']
    


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


class RecipeFormView(LoginRequiredMixin, View):

    def get(self, request):
        IngredientFormset = inlineformset_factory(Recipe, Ingredient, fields=('name',), extra=10, can_delete=False, formset=InlineFormSet)
        form = RecipeForm()
        formset = IngredientFormset()
        context = {
            'form': form,
            'formset': formset
        }
        return render(request, 'recipe_form.html', context)

    def post(self, request):
        IngredientFormset = inlineformset_factory(Recipe, Ingredient, fields=('name',), extra=10, can_delete=False, formset=InlineFormSet)
        form = RecipeForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            form.save()
        formset = IngredientFormset(request.POST, instance=instance)
        if formset.is_valid():
            formset.save()

        return redirect(reverse('dashboard'))

class RecipeUpdateView(LoginRequiredMixin, View):

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        IngredientFormset = inlineformset_factory(Recipe, Ingredient, fields=('name',), formset=InlineFormSet)
        form = RecipeForm(instance=recipe)
        

        formset = IngredientFormset(instance=recipe)
        context = {
            'form': form,
            'formset': formset,
            'recipe': recipe
        }
       
        return render(request, 'recipe_update_form.html', context)

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        IngredientFormset = inlineformset_factory(Recipe, Ingredient, fields=('name',), formset=InlineFormSet)
        form = RecipeForm(request.POST, instance=recipe)
        formset = IngredientFormset(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
        if formset.is_valid():
            formset.save()

        return redirect(reverse('dashboard'))


class DeleteView(LoginRequiredMixin, View):

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.delete()

        return redirect(reverse('dashboard'))

