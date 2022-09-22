
from django.urls import path, include
from .views import show_rentals, add_rental,show_customer, customer_alphabetical, add_customer, show_vehicles_by_group

urlpatterns = [

    path('rental', show_rentals, name='show_rental'),
    path('rental/add',add_rental, name="add_rental"),
    path('customer/<int:id>',show_customer,name='show_customer'),
    path('customer',customer_alphabetical, name="alphabetical"),
    path('customer/add',add_customer,name='add_customer'),
    path('vehicle',show_vehicles_by_group,name='show_vehicles')
]