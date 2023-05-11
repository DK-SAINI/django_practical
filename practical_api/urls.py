from django.urls import path
from practical_api import views

urlpatterns = [
    path('check_bearer', views.my_api_view, name="check_bearer")
]