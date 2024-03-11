import requests
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import TelegramMessage
import os


def send_telegram_message(chat_id, text):
    """
    This function sends a message to the Telegram chat
    using the sendMessage method.
    """
    telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    response = requests.post(
        f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage", data=payload
    )
    if response.ok:
        print(f"Message sent successfully {chat_id}")
    else:
        print(f"Sorry! Your message failed. Response: {response.text}")


def telegram_polling(request):
    """
    This function retrieves updates from
    the Telegram server, processes it and
    saves the received messages and chat id
    """
    # Telegram bot token retrieved from env
    telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    # Telegram bot chat id retrieved from env
    telegram_bot_chatid = os.environ.get("TELEGRAM_BOT_CHATID")
    # Get the latest update id from the database
    latest_update_id = (
        TelegramMessage.objects.latest("id").id
        if TelegramMessage.objects.exists()
        else None
    )
    # Prepare the request payload
    payload = {
        "offset": latest_update_id + 1 if latest_update_id else None,
        "timeout": 300,
    }
    # Make a request to the Telegram server to get updates
    response = requests.get(
        f"https://api.telegram.org/bot{telegram_bot_token}/getUpdates", params=payload
    )
    updates = response.json()["result"]
    # Process and save the received messages
    for update in updates:
        chat_id = update["message"]["chat"]["id"]
        message_text = update["message"]["text"]
        TelegramMessage.objects.create(chat_id=chat_id, message_text=message_text)
        # Send a response message to the chat
        response_text = f"Testing.......!"
        send_telegram_message(telegram_bot_chatid, response_text)
    # Respond to the Telegram server to acknowledge updates reciept
    return JsonResponse({"status": "ok"})


def test_telegram_message(request):
    telegram_bot_chatid = os.environ.get("TELEGRAM_BOT_CHATID")
    send_telegram_message(telegram_bot_chatid, 'Test message from the server...!')
    return HttpResponse('Test message sent successfully!')
