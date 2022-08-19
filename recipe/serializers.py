from rest_framework import serializers
from rest_framework.reverse import reverse
from recipe.models import Recipe, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id','name']



class RecipeAllSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Recipe
        fields = ['id', 'url', 'author', 'name', 'directions', 'image', 'ingredients']

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("recipe-all-detail", kwargs={'pk': obj.pk}, request=request)



class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    url = serializers.SerializerMethodField(read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Recipe
        fields = ['id', 'url', 'author', 'name', 'directions', 'image', 'ingredients']

        extra_kwargs = {"author": {"required": False, "allow_null": True}}



    def create(self, validated_data):
        ingredients = validated_data.pop('ingredients')
        recipe_instance = Recipe.objects.create(**validated_data)
        for ingredient in ingredients:
            Ingredient.objects.create(**ingredient, recipe=recipe_instance)
        return recipe_instance
    
    def update(self, instance, validated_data):
        ingredients_list = validated_data.pop('ingredients')
        instance.name = validated_data.get('name', instance.name)
        instance.directions = validated_data.get('directions', instance.directions)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        """getting list of hobbies id with same profile instance"""
        ingredients_with_same_recipe_instance = Ingredient.objects.filter(recipe=instance.pk).values_list('id', flat=True)

        ingredients_id_pool = []

        for ingredient in ingredients_list:
            if "id" in ingredient.keys():
                if Ingredient.objects.filter(id=ingredient['id']).exists():
                    ingredient_instance = Ingredient.objects.get(id=ingredient['id'])
                    ingredient_instance.name = ingredient.get('name', ingredient_instance.name)
                    ingredient_instance.save()
                    ingredients_id_pool.append(ingredient_instance.id)
                else:
                    continue
            else:
                ingredients_instance = Ingredient.objects.create(recipe=instance, **ingredient)
                ingredients_id_pool.append(ingredients_instance.id)

        for ingredient_id in ingredients_with_same_recipe_instance:
            if ingredient_id not in ingredients_id_pool:
                Ingredient.objects.filter(pk=ingredient_id).delete()

        return instance

    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("recipe-detail", kwargs={'pk': obj.pk}, request=request)
    


    





