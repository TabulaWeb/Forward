from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm
from shop.forms import MiniForm
from django.core.mail import send_mail


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})

    sent = False
    if request.method == 'POST':
        form = MiniForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = '{} Заказал звонок'.format(
                cd['name'])
            message = '{} заказл звонок, его номер - ({})'.format(
                cd['name'], cd['phome_number'])
            send_mail(subject, message, 'tabulaweb99@gmail.com',
                      ['tabulaweb99@gmail.com'])
            sent = True
            return redirect('shop:mail_ready')
    else:
        form = MiniForm()
    return render(request, 'cart/detail.html', {'cart': cart,
                                                'form': form,
                                                'categories': categories,
                                                'products': products,
                                                'category': category, })

