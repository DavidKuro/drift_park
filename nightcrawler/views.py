from django.shortcuts import render

# Create your views here.
def index(request):
    return render(render, 'crawler/index.html')

def cart(request):
    return render(render,'crawler/cart.html')

def checkout(request):
    return render(render, 'crawler/checkout.html')

def blog(request):
    return render(render,'crawler/blog.html')

def about(request):
    return render(render,'crawler/about.html')

def contact(request):
    return render(render,'crawler/contact.html')

def product(request):
    return render(render, 'crawlwe/product.html')


