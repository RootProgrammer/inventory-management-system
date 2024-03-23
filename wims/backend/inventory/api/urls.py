# inventory/api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.api import views
# from inventory.api.views import ItemListCreateAPIView

# If using viewsets and routers
router = DefaultRouter()
router.register(r'items', views.ItemViewSet)  # Handles CRUD for items

# URL patterns for your API
urlpatterns = [
    path('', include(router.urls)),  # Include router-generated URL patterns. This includes the `ItemViewSet` generated paths
    # Additional explicit API paths can be defined here, if not using viewsets or for custom endpoints
    # path('some-specific-endpoint/', views.some_specific_view),
    # path('items/', ItemListCreateAPIView.as_view(), name='item-list-create'),
]
