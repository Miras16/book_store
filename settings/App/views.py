from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
# from django.contrib.auth import authenticate,login
from .forms import NewUserForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User, auth
from django.db import IntegrityError
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username =username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm()
            return redirect('login')
    else: 
        form = AuthenticationForm()
        return render(request,template_name='App/login.html')
    

@csrf_exempt
def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        
        password = request.POST.get("password1")
        confirmation = request.POST.get("password2")
        if password != confirmation:
            return render(request, "App/registration.html", {
                "message": "Passwords must match."
            })
        elif len(password) < 8 and len(confirmation) < 8:
            return render(request, "App/registration.html", {
                "message": "Passwords must contain at least 8 characters."
            })
        elif password.isdigit() == True and confirmation.isdigit() == True:
            return render(request, "App/registration.html", {
                "message": "Passwords can't be entirely numeric."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "App/registration.html", {
                "message": "Email address already taken."
            })
        auth.login(request, user)
        return redirect("/")    
    else:
        return render(request, "App/registration.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def index(request):
    return render(request,'App/index.html')

def about(request):
    return render(request,'App/about.html')

def blog(request):
    return render(request, 'App/blog.html')

def contact(request):
    return render(request,'App/contact.html')

def shop(request):
    return render(request,'App/shop.html')

def single_post(request):
    return render(request, template_name='App/single-post.html')
    
def single_product(request):
    return render(request,'App/single-product.html')

def styles(request):
    return render(request,'App/styles.html')

def thankyou(request):
    return render(request,'App/thank-you.html')