from django.core.management.base import BaseCommand
from tele_chat.views import telegram_polling


class Command(BaseCommand):
    """
    Django management command to poll
    Telegram for updates and save
    messages to the database
    """
    help = "Poll Telegram for updates and save messages to the database"

    def handle(self, *args, **options):
        """
        Executes the command to poll Telegram
        for updates and saves messages to the database.
        """
        self.stdout.write(self.style.SUCCESS("Polling Telegram for updates..."))
        telegram_polling(None)
        self.stdout.write(self.style.SUCCESS("Polling complete."))
