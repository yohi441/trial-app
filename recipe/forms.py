from django import forms
from recipe.models import Recipe




class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'name',
            'image',
            'directions',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': "w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mb-3",
                'placeholder': str(field).replace('_', ' ').capitalize(),
            })


class InlineFormSet(forms.BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(InlineFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.fields['name'].widget.attrs.update({
                    'class': "w-full bg-white rounded border border-gray-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out mb-3",
                    'placeholder': 'Name'
                })
               



