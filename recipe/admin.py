from django.contrib import admin
from recipe.models import Recipe, Ingredient


class IngredientInline(admin.StackedInline):
    model = Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]