from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .form import ContactForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')
def cart(request):
    return render(request,'cart.html')

def shop(request):
    return render(request,'shop.html')
def checkout(request):
    return render(request,'checkout.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        users = authenticate(request, email=email, password=password)

        if users is not None:
            login(request, users)
            return redirect("/products/")
        else:
            return render(request, "login.html", {"error": "Invalid email or password"})

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")


def newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        # You can save this email to database later
        print(email)
        messages.success(request, "Successfully subscribed!")
        return redirect('login')

def contact(request):
    success = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("FORM IS VALID")
            form.save()   
            success = True
            form = ContactForm()  
    else:
        form = ContactForm()

    return render(request, "contact.html", {
        "form": form,
        "success": success
    })