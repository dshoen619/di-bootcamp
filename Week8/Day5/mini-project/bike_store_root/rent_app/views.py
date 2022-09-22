from django.shortcuts import render
from .models import Rental,Customer, Vehicle
from .forms import Add_Rental, Add_Customer, VehicleForm
from faker import Faker

def show_rentals(request):
    rentals=Rental.objects.all()

    return render(request, 'show_rentals.html',{'rentals':rentals})

def add_rental(request):
    fake=Faker()
    if request.method == 'POST':
        form_filled=Add_Rental(request.POST)
        if form_filled.is_valid():
            rental_date=fake.date()
            return_date=fake.date()
            customer =form_filled.cleaned_data['customer']
            vehicle=form_filled.cleaned_data['vehicle']

            new_rental=Rental(rental_date=rental_date,return_date=return_date,
            customer=customer, vehicle=vehicle)
            new_rental.save()
    
    context={'form':Add_Rental}
    return render(request,'add_rental.html', context)

def add_customer(request):
    form = Add_Customer()
    if request.method == 'POST':
        form=Add_Customer(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'add_rental.html',{'form':form})



def show_customer(request,id:int):
    customer_selected=Customer.objects.get(id=id)
    return render(request,'customer_id.html',{'customer':customer_selected})

def customer_alphabetical(request):
    customer_list=[]
    for i in Customer.objects.all():
        name= i.first_name +" "+i.last_name
        customer_list.append(name)
    
    context={'customer_list':sorted(customer_list)}

    return render(request, 'customer_alphabetical.html',context)

def show_vehicles_by_group(request):
    vehicle_group=Vehicle.objects.all()
    render(request, 'vehicles_by_type.html',{'group_dict':vehicle_group})


