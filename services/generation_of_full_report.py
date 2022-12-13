from typing import Type, Any

from django.db.models import QuerySet

from api.models import Mailing


def _generate_full_info(mailing_object: Type[Mailing],
                        mailing: QuerySet) -> dict[str, int | str | Any]:
    """
    Generates information about the number of mailings and their statuses
    :param mailing_object:
    :param mailing:
    :return:
    """
    export_dct = {"Mailing_count": len(mailing),
                  "Messages": ""}
    for mail in mailing:
        messages = {}
        entry_mail = mailing_object.objects.filter(mailing_id=mail.get("id")).all()
        sends = entry_mail.objects.filter(status="Sent").count()
        actives = entry_mail.objects.filter(status="Active").count()
        fails = entry_mail.objects.filter(status="Failed").count()
        messages["Message_count"] = len(entry_mail)
        messages["Sent"] = sends
        messages["Active"] = actives
        messages["Failed"] = fails
        export_dct["Messages"] = messages

    return export_dct
