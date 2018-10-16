from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login, logout

def home(request):
    return render(request, 'Users/home.html')

def signup_view(request):
    if request.method == 'POST': #If the user is creating a post, if the user already exist cause error, otherwise create the user form
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Users:home')
    else:
        form = UserCreationForm()
    return render(request, 'Users/signup.html', {'form': form})


def login_view(request): # Log the user in if authentication comes back true
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next')) #Continue onto page previously requested
            else:
                return redirect('Users:home')
    else:
        form = AuthenticationForm()
    return render(request, 'Users/login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("Users:home")
