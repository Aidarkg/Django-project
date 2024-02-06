from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from post.models import Product, Category, Review


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
    if request.method == 'GET':
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'Error')
        context = {
            "product": product
        }
        return render(request, 'products/detail_products.html', context)
