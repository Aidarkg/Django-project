from django import forms

from post.models import Product, Category, Review

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('photo', 'name', 'description', 'price', 'categories')
        labels = {
            'photo': "Фото",
            'name': 'Название',
            'description': 'Описание',
            'price': 'Цена',
            'categories': 'Категория'
        }
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': 'Название'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
        labels = {
            'text': 'Текст'
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
