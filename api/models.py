import zoneinfo

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


class Mailing(models.Model):
    date_start = models.DateTimeField("Mailing launch date")
    date_end = models.DateTimeField("Mailing end date")
    message_text = models.TextField("Message text", max_length=255)
    mobile_code = models.CharField("Search by mobile operator code",
                                   max_length=3,
                                   blank=True)
    tags = models.CharField("Search by tags", max_length=25, blank=True)

    @property
    def send_message(self):
        date_now = timezone.now()
        if self.date_start <= date_now <= self.date_end:
            return True
        else:
            return False

    def __repr__(self):
        return f"Mailing {self.id} from {self.date_start}"

    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"
        ordering = ["date_end"]


class Client(models.Model):
    TIMEZONE_CHOICE = list(zip(zoneinfo.available_timezones(),
                               zoneinfo.available_timezones()))

    phone_number_regex = RegexValidator(regex=r"^7\d{10}$",
                                        message="Client's phone number "
                                                "in the format [7XXXXXXXXXX] "
                                                "(X is a number from 0 to 9)")
    phone_number = models.CharField("Client's phone number",
                                    max_length=11,
                                    validators=[phone_number_regex],
                                    unique=True)
    mobile_code = models.CharField("Mobile operator code", max_length=3)
    tag = models.CharField("Search filtering tag", max_length=20, blank=True)
    timezone = models.CharField("Timezone",
                                max_length=50,
                                choices=TIMEZONE_CHOICE,
                                default="UTC")

    def save(self, *args, **kwargs):
        self.mobile_code = str(self.phone_number)[1:4]
        return super(Client, self).save(*args, **kwargs)

    def __repr__(self):
        return f"Client id - {self.id} with numbers {self.phone_number}"

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Message(models.Model):
    SENT = "sent"
    FAILED = "failed"
    ACTIVE = "active"

    STATUS_CHOICE = [
        (SENT, "Sent"),
        (FAILED, "Failed"),
        (ACTIVE, "Active")
    ]

    create_date = models.DateTimeField("Create date", auto_now_add=True)
    status = models.CharField("Sending status",
                              max_length=7,
                              choices=STATUS_CHOICE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name="messages")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="messages")

    def __repr__(self):
        return f"Message {self.id} for {self.client}. Message text: {self.mailing}"

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
