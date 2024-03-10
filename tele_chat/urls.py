from django.urls import path
from .views import telegram_polling

urlpatterns = [
    path('poll/', telegram_polling, name='telegram_polling'),
]
