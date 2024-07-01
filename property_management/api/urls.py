from django.urls import path
from .views import (
    PropertyAPI
)

urlpatterns = [
    path('get/<int:pk>/', PropertyAPI.as_view(), name='property-detail-api'),
    path('list/', PropertyAPI.as_view(), name='property-list-api'),
    path('create/', PropertyAPI.as_view(), name='property-create-api'),
    path('update/<int:pk>/', PropertyAPI.as_view(), name='property-update-api'),
    path('delete/<int:pk>/', PropertyAPI.as_view(), name='property-delete-api'),
]
