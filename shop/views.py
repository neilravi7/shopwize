from django.shortcuts import render
from django.db.models import Q
from products.models import Product, Category
# Create your views here.

# Create your views here.
# This is an home page view (starting or landing page)
def home(request):
    products = Product.objects.filter()[1:4]
    return render(
        request, 
        'shop/home.html', 
        {
            "products":products
            }
    )

def shop(request):
    products = Product.objects.filter()
    categories = Category.objects.filter()
    
    active_category = request.GET.get('category', None)
    query = request.GET.get('query', None)

    # Search by categories
    if active_category:
        specific_category = categories.filter(slug=active_category)[0]
        products = products.filter(category=specific_category)
    
    # Search by search terms    
    if query:
        products = products.filter(
            Q(name__icontains=query) |  
            Q(description__icontains=query) | 
            Q(category__name__icontains=query)
        ).distinct()    

    return render(request, 'shop/shop.html', context={
        "categories":categories,
        "products":products,
        "active_category":active_category,
        "total_items":len(products)
    })