from datetime import datetime
import os
import logging
from zoneinfo import ZoneInfo

from django.utils import timezone
from dotenv import load_dotenv
import requests

from api.models import Client, Mailing, Message
from notification_service.celery import app
from notification_service import settings

logging.basicConfig(level=logging.INFO, filename="services_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

load_dotenv()

URL = os.getenv("EXTERNAL_API_URL")
TOKEN = os.getenv("TOKEN")


@app.task(bind=True, retry_backoff=True)
def send_message(self, mailing_id: int,
                 client_id: int, json: dict,
                 url: str = URL, token: str = TOKEN):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    mailing = Mailing.objects.get(id=mailing_id)
    client = Client.objects.get(pk=client_id)
    message_id = json.get("id")

    if mailing.time_start > datetime.now(ZoneInfo(client.timezone)).time():
        hours_now = int(timezone.now().strftime("%H"))
        cooldown_time = (settings.HOURS_IN_DAY - (
                hours_now - int(mailing.time_start.strftime("%H"))
        )) * 3600
        logging.error(f"Message {message_id} will be sent in a {cooldown_time} of seconds")
        return self.retry(countdown=cooldown_time)
    try:
        requests.post(url=url + str(message_id), headers=headers, json=json)
        Message.objects.filter(pk=message_id).update(status="Sent")
        logging.info(f"Message {message_id} got status: 'Sent' ")
    except Exception as err:
        logging.info(f"Message {message_id} is failed")
        raise self.retry(err=err)
