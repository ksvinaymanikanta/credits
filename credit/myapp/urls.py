from django.urls import path
from .views import credit_card_application

urlpatterns = [
    path('myapp apply/', credit_card_application, name='credit_card_application'),  
]


