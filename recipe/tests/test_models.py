import pytest
from recipe.models import Recipe, Ingredient
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_recipe():
    user = User.objects.create(email="test@email.com", username="testuser", password="testpassword")
    recipe = Recipe.objects.create(author=user, name="test recipe name", directions="test directions")
    

    assert recipe.name == "test recipe name"
    assert recipe.directions == "test directions"
    assert recipe.image == None


@pytest.mark.django_db
def test_create_ingredients():
    user = User.objects.create(email="test@email.com", username="testuser", password="testpassword")
    recipe = Recipe.objects.create(author=user, name="test recipe name", directions="test directions")
    ingredient = Ingredient.objects.create(recipe=recipe, name="test ingredient")
    

    assert ingredient.name == "test ingredient"
    