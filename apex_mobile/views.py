from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Category, Product
from .forms import ClientRegistrationForm



def choice_picks(request):
    # Fetch all products from the database
    products = Product.objects.all()
    # Pass the products to the template using the context dictionary
    return render(request, 'apex_mobile/choice_picks.html', {'products': products})

def home_view(request):
    # Fetch data for sections
    categories = Category.objects.all()
    featured_products = Product.objects.filter(is_featured=True)
    top_deals = Product.objects.filter(is_top_deal=True)
    
    # Simple Search Execution
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(name__icontains=search_query) | Product.objects.filter(brand__icontains=search_query)
    else:
        products = Product.objects.all()

    # Process client registration form (Popup fallback/AJAX standard route)
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Welcome to Apex Mobile.")
            return redirect('home')
    else:
        form = ClientRegistrationForm()

    # Pull out recently viewed items from session array
    recently_viewed_ids = request.session.get('recently_viewed', [])
    recently_viewed_products = Product.objects.filter(id__in=recently_viewed_ids)

    context = {
        'categories': categories,
        'featured_products': featured_products,
        'top_deals': top_deals,
        'products': products,
        'search_query': search_query,
        'registration_form': form,
        'recently_viewed': recently_viewed_products,
    }
    return render(request, 'apex_mobile/home.html', context)


def product_detail_view(request, slug):
    """
    Renders product specifics and registers tracking behavior 
    to append item to the session history array.
    """
    product = get_object_or_404(Product, slug=slug)
    
    # Initialize list if missing
    if 'recently_viewed' not in request.session:
        request.session['recently_viewed'] = []
        
    session_list = request.session['recently_viewed']
    
    # Avoid duplicate tracking listings
    if product.id in session_list:
        session_list.remove(product.id)
        
    session_list.insert(0, product.id)
    request.session['recently_viewed'] = session_list[:4] # Store last 4 items
    request.session.modified = True

    return render(request, 'apex_mobile/product_detail.html', {'product': product})
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    # If the product is already in the cart, increment quantity
    if str(product.id) in cart:
        cart[str(product.id)]['quantity'] += 1
    else:
        cart[str(product.id)] = {'quantity': 1, 'price': str(product.price)}

    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail_view(request):
    cart = request.session.get('cart', {})
    return render(request, 'apex_mobile/cart_detail.html', {'cart': cart})

def choice_picks(request):
    return render(request, 'apex_mobile/choice_picks.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirects to home after login
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'apex_mobile/login.html')