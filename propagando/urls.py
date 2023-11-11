from django.urls import path
from propagando import views

app_name = 'propagando'

urlpatterns = [
    path('', views.home, name='home'),
]
