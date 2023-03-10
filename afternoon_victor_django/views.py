from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def aboutpage(request):
    return render(request, 'about us.html')


def blogpage(request):
    return render(request, 'blog.html')


def contactspage(request):
    return render(request, 'contacts.html')


def productspage(request):
    return render(request, 'products.html')


def servicespage(request):
    return render(request, 'services.html')
