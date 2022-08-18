from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from account.models import Account
from recipe.models import Recipe, Ingredient



class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'name',
            'image',
            'directions',
        ]


class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = [
            'name',
        ]



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': "w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mb-3"
    }))
    username = forms.CharField(required=True, min_length=4, max_length=10, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': "w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mb-3"
    }))
    password1 = forms.CharField(required=True, min_length=5, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': "w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mb-3"
    }))
    password2 = forms.CharField(required=True, min_length=5, widget=forms.PasswordInput(attrs={
        'placeholder': 'Re-type password',
        'class': "w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mb-3"
    }))

    class Meta:
        model = Account
        fields = ["email", "username", "password1", "password2"]


    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()   

        return user



class LoginForm(AuthenticationForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
         
        for field in self.fields:
            if field == 'username': # replace username placeholder to email
                self.fields[field].widget.attrs.update({
                    'class': "w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mb-3",
                    'placeholder': 'Email',
                    })
            else: # replace the underscore separator to space in the placeholder
                self.fields[field].widget.attrs.update({
                    'class': "w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mb-3",
                    'placeholder': field.replace('_', ' ').capitalize(),
                    })