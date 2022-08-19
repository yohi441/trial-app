
from django.shortcuts import render, redirect
from recipe.forms import RecipeForm, InlineFormSet
from django.urls import reverse
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from recipe.models import Ingredient, Recipe
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from django.contrib import messages




class IndexView(ListView):
    model = Recipe
    template_name = "index.html"
    paginate_by = 6
    context_object_name = 'recipes'
    ordering = ['created']
    


class DashboardView(LoginRequiredMixin, ListView):
    login_url = '/signin/'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)

    model = Recipe
    template_name = "dashboard.html"
    paginate_by = 5
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
    login_url = '/signin/'

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
        form = RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            form.save()
            formset = IngredientFormset(request.POST, instance=instance)
            if formset.is_valid():
                formset.save()
            messages.success(request, "Recipe Create Successfully")
        else:
            messages.error(request, "Error Has Occured Please Try Again")

        return redirect(reverse('dashboard'))

class RecipeUpdateView(LoginRequiredMixin, View):
    login_url = '/signin/'

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
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        formset = IngredientFormset(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            if formset.is_valid():
                formset.save()
            messages.success(request, "Recipe Updated Successfully")
        else:
            messages.error(request, "Error Has Occured Please Try Again")

        return redirect(reverse('dashboard'))


class DeleteView(LoginRequiredMixin, View):
    login_url = '/signin/'

    def post(self, request, pk):
        try:
            recipe = get_object_or_404(Recipe, pk=pk)
            recipe.delete()
            messages.success(request, "Recipe Delete Successfully")
        except:
            messages.error(request, "Error Has Occured Please Try Again")
            
        return redirect(reverse('dashboard'))

