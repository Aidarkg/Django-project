from typing import Any
from django.http import HttpResponse
from datetime import datetime
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied

from post.models import Product, Category, Review
from post.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm


def hello_view(request):
    if request.method == 'GET':
        return HttpResponse("Hello! It`s my project")


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello! It`s my project")


def get_current_time(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'date_time.html', {'current_time': current_time})


def goodbye_view(request):
    if request.method == 'GET':
        return HttpResponse("Goodbye user!")


def main_view(request):
    return render(request, 'layouts/index.html')


class ProductView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        queryset = self.get_queryset()
        paginator =  Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page', 1)
        page_ogj = paginator.get_page(page)
        context['max_page'] = page_ogj
        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        sort = self.request.GET.get('sort', 'price')
        category = self.request.GET.get('category', '')

        if search:
            queryset = queryset.filter(
                Q(name__contains=search) |
                Q(description__contains=search)
            )
        if sort:
            queryset = queryset.order_by(sort)
        if category:
            queryset = queryset.filter(categories__id=category)

        return queryset
    
    # def handle_no_permission(self):
    #     if self.raise_exception:
    #         raise PermissionDenied(self.get_permission_denied_message())
    #     return HttpResponseForbidden("У вас нет разрешения на доступ к этой странице.")


class ProductDeatilView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products/detail_products.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewCreateForm()
        context['has_change_permission'] = (context['object'].user == self.request.user)
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/create_product.html'
    context_object_name = 'product'
    success_url = '/products/'

    def get_absolute_url(self):
        if self.request.user.is_authenticated():
            return reverse('products_list')
        return reverse('login')


class CategoryView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    template_name = 'categories/create_category.html'
    success_url = '/categories/'

    def get_absolute_url(self):
        if self.request.user.is_authenticated():
            return reverse('categories_list')
        return reverse('login')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCreateForm
    template_name = 'products/edit_product.html'
    pk_url_kwarg = 'product_id'
    success_url = '/products/'

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        if product.user != request.user:
            return HttpResponse('Permission denied', status=403)
        return super().get(request, *args, **kwargs)



# @login_required(login_url='/login/')
# def products_view(request):
#     if request.method == 'GET':
#         search = request.GET.get('search', '')
#         sort = request.GET.get('sort', 'price')
#         category = request.GET.get('category', '')
#         page = request.GET.get('page', 1)

#         products = Product.objects.all()
#         # products = Product.objects.all().exclude(user = request.user)

#         if search:
#             products = products.filter(
#                 Q(name__contains=search) |
#                 Q(description__contains = search)
#             )

#         if sort:
#             products = products.order_by(sort)

#         if category:
#             products = products.filter(categories__id=category)

#         limit = 3
#         max_page = products.__len__() / limit
#         if round(max_page) < max_page:
#             max_page = round(max_page) + 1 
#         else:
#             max_page = round(max_page)
        
#         start = (int(page) - 1) * limit
#         end = start + limit

#         products = products[start:end]


#         categories = Category.objects.all()
#         context = {"products": products, 'categories': categories, 'max_page': range(1, max_page + 1)}
#         return render(
#             request,
#             'products/products.html',
#             context)

# def category_view(request):
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         context = {'categories': categories}
#         return render(
#             request,
#             'categories/category_list.html',
#             context
#         )


# def product_detail_view(request, product_id):
#     form = ReviewCreateForm()
#     product = get_object_or_404(Product, id=product_id)

#     has_change_permission = (product.user == request.user)

#     context = {
#         "product": product,
#         'review_form': form,
#         'has_change_permission': has_change_permission
#     }

#     return render(request, 'products/detail_products.html', context)


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


# @login_required
# def product_create_view(request):
#     if request.method == 'POST':
#         form = ProductCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.user = request.user
#             form.save() 
#             return redirect('products_list')
#         else:
#             print(form.errors)
#     else:
#         form = ProductCreateForm()
#     return render(request, 'products/create_product.html', {'form': form})


# @login_required
# def category_create_view(request):
#     if request.method == 'POST':
#         form = CategoryCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('categories_list')
#     else:
#         form = CategoryCreateForm()
#     context = {'form': form}
#     return render(request, 'categories/create_category.html', context)


# @login_required
# def product_update_view(request, product_id):
#     try:
#         product = Product.objects.get(id=product_id)
#     except Product.DoesNotExist:
#         return render(request, 'errors/404.html')
    
#     if product.user != request.user:
#         return HttpResponse('Permission denied', status=403)
    
#     if request.method == 'GET':
#         form = ProductCreateForm(instance=product)
#         return render(request, 'products/edit_product.html', {'form': form})
    
#     elif request.method == 'POST':
#         form = ProductCreateForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('products_list')
#         else:
#             print(form.errors)
#         return render(request, 'products/edit_product.html', {'form': form})