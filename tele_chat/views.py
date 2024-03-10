import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import TelegramMessage
import os

telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")


@csrf_exempt
@require_POST
def telegram_webhook(request):
    # This function handles incoming messages
    data = json.loads(request.body.decode("utf-8"))
    # Extract relevant information from the Telegram update
    chat_id = data["message"]["chat"]["id"]
    message_text = data["message"]["text"]
    # Save message to the database
    TelegramMessage.objects.create(chat_id=chat_id, message_text=message_text)
    # Respond to the Telegram server to acknowledge message receipt
    return JsonResponse({"status": "ok"})
