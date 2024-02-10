from django import forms

from post.models import Product, Category, Review

class ProductCreateForms(forms.ModelForm):
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


class CategoryCreateForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name': 'Название'
        }


class ReviewCreateForms(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
        labels = {
            'text': 'Текст'
        }