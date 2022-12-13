import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import Client, Mailing, Message
from .integration_with_external_api import send_message

logging.basicConfig(level=logging.INFO, filename="services_log.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


@receiver(signal=post_save, sender=Mailing)
def request_mailing(sender, instance=None, created=False, **kwargs):
    if created:
        mailing = Mailing.objects.filter(id=instance.id).first()
        clients = Client.objects.filter(mobile_code=mailing.mobile_code,
                                        tag__exact=mailing.tags).all()
        logging.info(f"Start mailing {mailing.id} at {mailing.time_start}")
        for client in clients:
            message = Message.objects.create(
                status="Active",
                client_id=client.id,
                mailing_id=instance.id
            )
            logging.info(f"Create message {message.id}")
            data = {
                "id": message.id,
                "phone": client.phone_number,
                "text": mailing.message_text
            }

            if instance.to_send:
                logging.info(f"Message {message.id} send to {client.id} with phone numbers {client.phone_number}")
                send_message.apply_async((data, client.id, mailing.id),
                                         expires=mailing.date_end)
            else:
                send_message.apply_async((data, client.id, mailing.id),
                                         eta=mailing.date_start,
                                         expires=mailing.date_end)
