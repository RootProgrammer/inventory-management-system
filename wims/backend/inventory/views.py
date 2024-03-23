from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt  # Use csrf_exempt for demonstration
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


@csrf_exempt  # Use csrf_exempt for custom login_view for demonstration
def base(request):
    return render(request, "base.html")


@login_required
def home_view(request):
    return render(request, "home.html")


"""
if you want to customize the redirect URL for unauthenticated users 
(for example, if your login route has a different name or you want to append a query string)
you can pass the login_url parameter to the decorator:

@login_required(login_url='/accounts/login/')
def home_view(request):
    return render(request, 'home.html')

"""


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Initialize an error dictionary to hold validation errors
        errors = {}

        # Check if passwords match
        if password1 != password2:
            errors['password_mismatch'] = "The two password fields didn't match."

        # Validate the password
        try:
            validate_password(password1, user=User(username=username))
        except ValidationError as e:
            errors['password_error'] = e.messages

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            errors['username'] = "A user with that username already exists."

        # If there are no errors, create the user
        if not errors:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            login(request, user)  # Log the user in
            return redirect('home')
        else:
            # Pass the errors back to the template
            return render(request, 'signup.html', {'errors': errors})

    return render(request, 'signup.html')


def login_view(request):
    error_message = None  # Initialize error message
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Invalid username or password."  # Set error message

    return render(request, 'login.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    # Redirect to login page, home page, or another appropriate page
    return redirect('base')


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="API documentation for the project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
"""
Secure Your API Documentation[Optional]
If you want to restrict access to your API documentation, you can adjust the permission_classes in the schema_view.
For instance, using permissions.IsAuthenticated would require users to be logged in to view the documentation.
"""