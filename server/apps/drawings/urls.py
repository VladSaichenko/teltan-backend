from django.urls import path
from .views import get_tickets_redemption_amount

urlpatterns = [
    path('api/get-tickets-redemption-amount/<int:pk>', get_tickets_redemption_amount)
]
