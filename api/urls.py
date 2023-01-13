from django.urls import path
from .views import PropertyAPI


app_name = "api"

urlpatterns = [
    path('', PropertyAPI.as_view(), name="api"),
    path('update-property-view/<int:pk>/', PropertyAPI.as_view(), name="update-property-view"),
]