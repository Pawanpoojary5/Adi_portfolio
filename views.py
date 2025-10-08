from django.shortcuts import render

# Home page
def home(request):
    return render(request, "home.html")

# About page
def about(request):
    return render(request, 'about.html')

# Services page
def services(request):
    return render(request, 'services.html')

# Contact page
def contact(request):
    return render(request, 'contact.html')

# Portfolio/Work page
def portfolio(request):
    return render(request, 'portfolio.html')

# Upload page
def upload(request):
    return render(request, 'upload.html')