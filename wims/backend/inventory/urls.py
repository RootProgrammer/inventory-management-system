# In your app's urls.py (e.g., inventory/urls.py)
from django.urls import path
from inventory.views import base, home_view, signup, login_view, logout_view  # Make sure you have these views

urlpatterns = [
    path('', base, name='base'),
    path('home/', home_view, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
