from django.urls import path, include
from recipe import views, api_views
from account import views as account_views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', account_views.SignupView.as_view(), name='signup'),
    path('signin/', account_views.SigninView.as_view(), name='signin'),
    path('signout/', account_views.SignoutView.as_view(), name='signout'),
    path('success/', account_views.SignupSuccessView.as_view(), name='success'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('recipe/form/', views.RecipeFormView.as_view(), name='recipe-form'),
    path('recipe/delete/<int:pk>/', views.DeleteView.as_view(), name='recipe-delete'),
    path('recipe/update/<int:pk>/', views.RecipeUpdateView.as_view(), name='recipe-update'),
]

api_urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api/', api_views.api_root, name='api-root'),
    path('api/recipes/all/', api_views.RecipeAllList.as_view(), name=api_views.RecipeAllList.name),
    path('api/recipe/detail/<int:pk>/', api_views.RecipeAllDetail.as_view(), name=api_views.RecipeAllDetail.name),
    path('api/recipe/list/', api_views.RecipeList.as_view(), name=api_views.RecipeList.name),
    path('api/recipe/<int:pk>/', api_views.RecipeDetail.as_view(), name=api_views.RecipeDetail.name),
  
]


urlpatterns += api_urlpatterns

