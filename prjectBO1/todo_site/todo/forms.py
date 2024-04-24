from django import forms
from .models import Todo, Category, CategoryChoice


class Todo_Form(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"

class TodoCategoryForm(forms.Form):
    CATEGORY_CHOICES = [(c.id, c.name) for c in Category.objects.all()]
    CATEGORY_CHOICES.append(('', 'Custom'))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    custom_category = forms.CharField(required=False)

    def clean_category(self):
        category = self.cleaned_data['category']
        if category == '':
            raise forms.ValidationError('Please select a category')
        return category