from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Ourprojects, Engineer_tips
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def our_projects(request, category_slug=None):
    category = None
    posts = Ourprojects.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/our_projects.html', {'category': category,
                                                              'categories': categories,
                                                              'products': products,
                                                              'posts': posts})

def ourprojects_detail(request, year, month, day, post):
    post = get_object_or_404(Ourprojects, slug=post, publish__year=year,
                          publish__month=month, publish__day=day)
    return render(request, 'shop/product/ourprojects_detail.html', {'post': post})

def engineer_tips(request, category_slug=None):
    category = None
    engineertips = Engineer_tips.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/engineer_tips.html', {'category': category,
                                                               'categories': categories,
                                                               'products': products,
                                                               'engineertips': engineertips})


def delivery(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/delivery.html', {'category': category,
                                                          'categories': categories,
                                                          'products': products})


def reviews(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/reviews.html', {'category': category,
                                                         'categories': categories,
                                                         'products': products})


def contacts(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/contacts.html', {'category': category,
                                                         'categories': categories,
                                                         'products': products})

