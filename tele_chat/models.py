from django.db import models


class TelegramMessage(models.Model):
    #  This class stores telegram messages
    chat_id = models.CharField(max_length=255)
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chat_id} - {self.message_text}"
