from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

from .models import Mailing, Client, Message
from .serializers import MailingSerializer, ClientSerializer, MessageSerializer
from services.generation_of_full_report import _generate_full_info


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    @action(detail=True,
            methods=["GET"],
            url_path='info',
            url_name='mailing_info')
    def get_info(self, request, pk) -> Response:
        """
        Information data about specific mailing
        :param request:
        :param pk:
        :return Response:
        """
        mailing = get_object_or_404(Mailing, pk=pk)
        serializer = MailingSerializer(mailing)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False,
            methods=["GET"],
            url_path='info',
            url_name='mailing_full_info')
    def get_full_info(self, request) -> Response:
        """
        Information data about all mailing
        :param request:
        :return:
        """

        mailing = Mailing.objects.all()

        info = _generate_full_info(Mailing, mailing)
        return Response(info, status=status.HTTP_200_OK)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
