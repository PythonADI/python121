from django.shortcuts import render
from store.models import Product

# Create your views here.
def product_list_view(request):
    return render(
        request,
        "store/product_list.html",
        {
            "products": Product.objects.all()
        }
    )