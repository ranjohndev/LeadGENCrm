from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_view, name='test'),  # Example URL pattern for the test view
    # Add more URL patterns as needed for other views
]
