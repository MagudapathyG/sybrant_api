# myproject/urls.py
from django.urls import path
from .views import ProfileFilterView

urlpatterns = [
    path('profiles/', ProfileFilterView.as_view(), name='profile_filter'),
]
