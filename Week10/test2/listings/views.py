from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator

def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator= Paginator(listings,3)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    context = {
        'listings':paged_listings,'latest_listings':Listing.objects.all()[:3]
    }
    return render(request, 'listings/listings.html',context)

def listing (request, listing_id):
    
    listing = Listing.objects.get(id=listing_id)

    context ={
        'listing':listing
    }
    return render(request, 'listings/listing.html',context)

def search(request):
    from listings.choices import bedroom_choices, state_choices,price_choices

    queryset_list=Listing.objects.order_by('-list_date')

    #keywords
    if 'keyword' in request.GET:
        keyword= request.GET['keywords']
        if keyword:
            queryset_list=queryset_list.filter(keyword=keyword)

    #City
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            queryset_list=queryset_list.filter(city=city)

    #state
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state=state)

    #bedrooms
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms=bedrooms)

    #price 
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            queryset_list=queryset_list.filter(price=price)



    context={
        'state_choices': state_choices,
        'bedroom_choices':bedroom_choices,
        'price_choices':price_choices,
        'listings':queryset_list,
        'values':request.GET
    }


    return render(request, 'listings/search.html',context)
 

def latest_listings(request):
    listings=Listing.objects.all()[:3]
    context={
        'listings':listings
    }
    return render(request, 'home.html',context)