from django.urls import path
from recipe import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('signout/', views.SignoutView.as_view(), name='signout'),
    path('success/', views.SignupSuccessView.as_view(), name='success'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('recipe/form/', views.RecipeFormView.as_view(), name='recipe-form'),
    path('recipe/delete/<int:pk>/', views.DeleteView.as_view(), name='recipe-delete'),
    path('recipe/update/<int:pk>/', views.RecipeUpdateView.as_view(), name='recipe-update'),
]
