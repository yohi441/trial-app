from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from recipe.models import Recipe
from recipe.serializers import RecipeSerializer, RecipeAllSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser


@api_view(['GET',])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    queryset=''
    return Response({
    'all-recipes': reverse('recipe-all-list', request=request, format=format),
    'user-recipe-list': reverse('recipe-list', request=request, format=format)
})

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    name = 'recipe-list'

class RecipeAllList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeAllSerializer
    name = 'recipe-all-list'

class RecipeAllDetail(generics.RetrieveAPIView):
    serializer_class = RecipeAllSerializer
    queryset = Recipe.objects.all()
    name = 'recipe-all-detail'

class RecipeList(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)

    queryset = Recipe.objects.all()

    name = 'recipe-list'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = RecipeSerializer
    permission_classes = (IsAuthenticated,)

    queryset = Recipe.objects.all()
    
    name = 'recipe-detail'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)