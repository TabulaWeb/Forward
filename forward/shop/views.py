from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Ourprojects, Engineer_tips, Comment
from cart.forms import CartAddProductForm
from .forms import CommentForm, MiniForm, MessageForm
from django.core.mail import send_mail

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

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
            return redirect('/')
    else:
        form = MiniForm()

    sent = False
    if request.method == 'POST':
        form_message = MessageForm(request.POST)
        if form_message.is_valid():
            cd = form_message.cleaned_data
            subject = '{} написал вам сообщение'.format(
                cd['MessageName'])
            message = 'Вам написал {}, его номер - ({}) и email - {}\n\nТекст Сообщения: {}'.format(
                cd['MessageName'], cd['MessagePhomenumber'], cd['MessageEmail'], cd['message'])
            send_mail(subject, message, 'tabulaweb99@gmail.com',
                      ['tabulaweb99@gmail.com'])
            sent = True
            return redirect('/')
    else:
        form_message = MessageForm()
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'cart_product_form': cart_product_form,
                   'categories': categories,
                   'products': products,
                   'form': form,
                   'form_message':form_message,})


def product_detail(request, id, slug, category_slug=None):
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
    else:
        form = MiniForm()
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_form': cart_product_form,
                   'form': form,})


def our_projects(request, category_slug=None):
    category = None
    posts = Ourprojects.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
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
    else:
        form = MiniForm()
    return render(request, 'shop/product/our_projects.html', {'category': category,
                                                              'categories': categories,
                                                              'products': products,
                                                              'posts': posts,
                                                              'form': form,})

def ourprojects_detail(request, year, month, day, post, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    post = get_object_or_404(Ourprojects, slug=post, publish__year=year,
                          publish__month=month, publish__day=day)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
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
    else:
        form = MiniForm()
    return render(request, 'shop/product/ourprojects_detail.html', {'post': post,
                                                                    'category': category,
                                                                    'categories': categories,
                                                                    'products': products,
                                                                    'form': form,})

def engineer_tips(request, category_slug=None):
    category = None
    engineertips = Engineer_tips.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
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
    else:
        form = MiniForm()
    return render(request, 'shop/product/engineer_tips.html', {'category': category,
                                                               'categories': categories,
                                                               'products': products,
                                                               'engineertips': engineertips,
                                                               'form': form,})


def delivery(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
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
    else:
        form = MiniForm()
    return render(request, 'shop/product/delivery.html', {'category': category,
                                                          'categories': categories,
                                                          'products': products,
                                                          'form': form,})


def reviews(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    comments = Comment.objects.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()
        return redirect('/reviews/')
    else:
        comment_form = CommentForm()

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
    else:
        form = MiniForm()
    return render(request, 'shop/product/reviews.html', {'category': category,
                                                         'categories': categories,
                                                         'products': products,
                                                         'comments': comments,
                                                         'new_comment': new_comment,
                                                         'comment_form': comment_form,
                                                         'form': form,})


def contacts(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
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
    else:
        form = MiniForm()

    sent = False
    if request.method == 'POST':
        form_message = MessageForm(request.POST)
        if form_message.is_valid():
            cd = form_message.cleaned_data
            subject = '{} написал вам сообщение'.format(
                cd['MessageName'])
            message = 'Вам написал {}, его номер - ({}) и email - {}\n\nТекст Сообщения: {}'.format(
                cd['MessageName'], cd['MessagePhomenumber'], cd['MessageEmail'], cd['message'])
            send_mail(subject, message, 'tabulaweb99@gmail.com',
                      ['tabulaweb99@gmail.com'])
            sent = True
    else:
        form_message = MessageForm()
    return render(request, 'shop/product/contacts.html', {'category': category,
                                                         'categories': categories,
                                                         'products': products,
                                                         'form': form,
                                                         'form_message': form_message})

