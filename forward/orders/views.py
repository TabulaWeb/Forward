from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.forms import MiniForm
from decimal import Decimal
from django.core.mail import send_mail

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            # Очищаем корзину.
            
            cd = form.cleaned_data
            subject = 'Новый заказ от {} {}, его номер - {}'.format(cd['first_name'], cd['last_name'], cd['phone_number'])
            m = []
            for item in cart:
                mess = '{} - {}\nСумма заказа = {}\n\n'.format(item['quantity'], item['product'], item['total_price'])
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
    return render(request, 'orders/order/create.html', {'cart': cart, 'form':form, 'form_mini':form_mini})

