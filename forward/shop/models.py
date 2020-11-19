from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)
    arenda = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])

class SubCategory(models.Model):
    categorychange = models.ForeignKey(Category,
                                       related_name='SubCategory',
                                       on_delete=models.CASCADE)
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(SubCategory,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    description = models.TextField(blank=True)
    arenda = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])

class Ourprojects(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
    )
    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    body = models.TextField() 
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)
    one_slide = models.ImageField(upload_to='products/%Y/%m/%d',
                                  blank=True)
    two_slide = models.ImageField(upload_to='products/%Y/%m/%d',
                                  blank=True)
    three_slide = models.ImageField(upload_to='products/%Y/%m/%d',
                                    blank=True)
    four_slide = models.ImageField(upload_to='products/%Y/%m/%d',
                                   blank=True)
    five_slide = models.ImageField(upload_to='products/%Y/%m/%d',
                                   blank=True)

    def __str__(self): 
        return self.title

    def get_absolute_url(self):
        return reverse('shop:ourprojects_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

class Engineer_tips(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()

class Comment(models.Model):
    name = models.CharField(max_length=80, verbose_name='Имя')
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)

    
