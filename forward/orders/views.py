from django.shortcuts import render
from .models import OrderItem
from shop.models import Product, Category, SubCategory
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.forms import MiniForm
from decimal import Decimal
from django.core.mail import send_mail


def order_create(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    subcategories = SubCategory.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            # Очищаем корзину.
            
            cd = form.cleaned_data
            subject = 'Новый заказ от {} {}, его номер - {}'.format(cd['first_name'], cd['last_name'], cd['phone_number'])
            m = []
            for item in cart:
                if (item['product'].arenda == True):
                    mess = 'АРЕНДА\nКол-во товара:{} - Товар:{}\nСумма заказа = {}\n\n'.format(item['quantity'], item['product'], item['total_price'])
                    m.append(mess)
                else:
                    mess = 'ПОКУПКА\nКол-во товара:{}\nТовар:{}\nСумма заказа = {}\n\n'.format(item['quantity'], item['product'], item['total_price'])
                    m.append(mess)
            message = ' '.join(m)
            send_mail(subject, message, 'tabulaweb99@gmail.com', ['tabulaweb99@gmail.com'])
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    if request.method == 'POST':
        form_mini = MiniForm(request.POST)
        if form_mini.is_valid():
            cd = form_mini.cleaned_data
            subject = '{} Заказал звонок'.format(
                cd['name'])
            message = '{} заказл звонок, его номер - ({})'.format(
                cd['name'], cd['phome_number'])
            send_mail(subject, message, 'tabulaweb99@gmail.com',
                      ['tabulaweb99@gmail.com'])
            sent = True
            return redirect('shop:mail_ready')
    else:
        form_mini = MiniForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'subcategories': subcategories, 'form': form, 'form_mini': form_mini, 'category': category, 'categories': categories, 'products': products, })

