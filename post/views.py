from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from post.models import Product, Category, Review
from post.forms import ProductCreateForms, CategoryCreateForms, ReviewCreateForms


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! Its my project")


def data_view(request):
    if request.method == 'GET':
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Current date and time: {formatted_date}")


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")


def main_view(request):
    return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {"products": products}
        return render(
            request,
            'products/products.html',
            context)


def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(
            request,
            'categories/category_list.html',
            context
        )


def product_detail_view(request, product_id):
    form = ReviewCreateForms()
    
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'Error')
        context = {
            "product": product,
            'review_form': form
        }
        return render(
            request, 
            'products/detail_products.html', 
            context)


def review_create_view(request, product_id):
    if request.method == "POST":
        form = ReviewCreateForms(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = product_id
            review.save()
        
        return redirect('product_detail', product_id=product_id)


def product_create_view(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForms()
        }

        return render(
            request,
            'products/create_product.html',
            context=context
        )

    elif request.method == 'POST':
        form = ProductCreateForms(request.POST, request.FILES)

        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            # form.save()
            return redirect('products_list')

        context = {
            'form': ProductCreateForms()
        }

        return render(
            request,
            'products/create_product.html',
            context=context
        )
    

def category_create_view(request):
    if request.method == 'GET':
        context = {
            'form': CategoryCreateForms
        }
        return render(
            request,
            'categories/create_category.html',
            context
        )
    elif request.method == 'POST':
        name = request.POST.get('name')

        category = Category.objects.create(
            name=name
        )

        return HttpResponse(f'Категория {category.id} создан')

