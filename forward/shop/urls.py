from django.urls import path
from . import views
app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    
    path('our_projects/', views.our_projects, name='our_projects'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.ourprojects_detail, name='ourprojects_detail'),
    path('engineer_tips/', views.engineer_tips, name='engineer_tips'),
    path('delivery/', views.delivery, name='delivery'),
    path('reviews/', views.reviews, name='reviews'),
    path('contacts/', views.contacts, name='contacts'),
    path('mail_ready/', views.mail_ready, name='mail_ready'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_subcategory, name='subcategory'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
