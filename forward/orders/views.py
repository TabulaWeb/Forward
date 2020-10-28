from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.forms import MiniForm
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
            cart.clear()
            # cd = form.cleaned_data
            # subject = 'Новый заказ'
            # message = '{} {} заказал у вас\n{} - {}\nСумма заказа = {}\nЕго номер телефона - {}'.format(cd['first_name'], cd['last_name'], item['quantity'], item['product'], item['price'], cd['phone_number'])
            # send_mail(subject, message, 'tabulaweb99@gmail.com',
            #           ['tabulaweb99@gmail.com'])
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
    else:
        form_mini = MiniForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form':form, 'form_mini':form_mini})

