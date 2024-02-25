from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from post.models import Product, Category, Review
from post.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm
from django.contrib.auth.decorators import login_required


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! It`s my project")


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

@login_required
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
    form = ReviewCreateForm()
    product = get_object_or_404(Product, id=product_id)
    context = {
        "product": product,
        'review_form': form
    }
    return render(request, 'products/detail_products.html', context)


@login_required
def review_create_view(request, product_id):
    if request.method == "POST":
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = product_id
            review.user = request.user
            review.save()

    return redirect('product_detail', product_id=product_id)


@login_required
def product_create_view(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            form.save() 
            return redirect('products_list')
        else:
            print(form.errors)
    else:
        form = ProductCreateForm()
    return render(request, 'products/create_product.html', {'form': form})


@login_required
def category_create_view(request):
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_list')
    else:
        form = CategoryCreateForm()
    context = {'form': form}
    return render(request, 'categories/create_category.html', context)

