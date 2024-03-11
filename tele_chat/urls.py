from django.urls import path
from .views import telegram_polling, test_telegram_message

urlpatterns = [
    path("poll/", telegram_polling, name="telegram_polling"),
    path("test_telegram_message/", test_telegram_message, name="test_telegram_message"),
]
