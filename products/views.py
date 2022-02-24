from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, SubCategory

# Create your views here.
def all_products(request):
    """ View to return all products, and sorting and searching """

    products = Product.objects.all()
    query = None
    categories = None
    SubCategory = None
    subcategory = None

    if request.GET:
        if 'Category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)

        if 'sub_categories' in request.GET:
            subcategory = request.GET['sub_categories']
            products = products.filter(subcategory__name=subcategory)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything!")
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) | Q(product_description__icontains=query)
            )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_subcategory': subcategory
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show indivdual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)