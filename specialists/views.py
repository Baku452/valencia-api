import os
import logging
from dotenv import load_dotenv

load_dotenv(override=True)
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail, send_mass_mail

from .models import ContactUs, Newsletter
from .serializers import (
    ContactUsSerializer,
    NewsletterSerializer,
    ContactUsB2BSerializer,
    ContactUsB2CSerializer,
    TailorFormSerializer,
)

logger = logging.getLogger(__name__)
subject = "Web Opportunity "
subjectTailor = "Web Opportunity Tailor Made"
subjectB2CPromo = "Promo Web Opportunity B2C "
subjectB2C = "Web Opportunity B2C "
subjectB2BPromo = "Promo Web Opportunity B2B "
subjectB2B = "Web Opportunity B2B "
html_message = render_to_string("mail_template.html", {"context": "values"})
plain_message = strip_tags(html_message)
from_email = os.getenv("DJANGO_FROM_MAIL")
to = os.getenv("DJANGO_TO_MAIL").split(",")


class ContactCreateApi(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            send_mail(
                subject + serializer.data["destination_interest"],
                plain_message,
                serializer.data["first_name"]
                + " "
                + serializer.data["last_name"]
                + from_email,
                to,
                html_message=render_to_string("contactTemplate.html", serializer.data),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactB2CCreateApi(APIView):
    def post(self, request):
        serializer = ContactUsB2CSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_mail(
                subjectB2C + serializer.data["package"],
                plain_message,
                serializer.data["first_name"]
                + " "
                + serializer.data["last_name"]
                + from_email,
                to,
                html_message=render_to_string(
                    "contactTemplateB2C.html", serializer.data
                ),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            logger.warning('Error creating B2C contact \n'
            +str(serializer.data["first_name"]) +" \n"
            +str(serializer.data["last_name"]) +" \n"
            +str(serializer.data["email"]) +" \n"
            +str(serializer.data["message"]) +" \n"
            +str(serializer.errors))
            send_mail(
                "Error Django Contact B2C",
                str(serializer.data["package"]) +"\n"
                +str(serializer.data["first_name"])  +" \n"
                +str(serializer.data["last_name"]) +" \n"
                +str(serializer.data["email"]) +" \n"
                +str(serializer.data["message"]) +" \n"
                + "Errors :" + "\n"
                +str(serializer.errors) +" \n"
                ,
                from_email,
                [from_email],
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactB2BCreateApi(APIView):
    def post(self, request):
        serializer = ContactUsB2BSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print(serializer.data["is_promo"])
            send_mail(
                subjectB2BPromo + serializer.data["package"]
                if serializer.data["is_promo"]
                else subjectB2B + serializer.data["package"],
                plain_message,
                serializer.data["company"] + from_email,
                to,
                html_message=render_to_string(
                    "contactTemplateB2B.html", serializer.data
                ),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TailorMadeCreateApi(APIView):
    def post(self, request):
        serializer = TailorFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            send_mail(
                subjectTailor,
                plain_message,
                serializer.data["first_name"]
                + " "
                + serializer.data["last_name"]
                + from_email,
                to,
                html_message=render_to_string("tailor_made.html", serializer.data),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsletterListApi(APIView):
    def get(self, request, format=None):
        suscriptores = Newsletter.objects.all()
        serializer = NewsletterSerializer(suscriptores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsletterDetailApi(APIView):
    def get_object(self, email):
        try:
            return Newsletter.objects.get(email=email)
        except Newsletter.DoesNotExist:
            raise Http404

    def get(self, request, email):
        subscriptor = self.get_object(email)
        serializer = NewsletterSerializer(subscriptor)
        return Response(serializer.data)

    def delete(self, request, email):
        subcriptor = self.get_object(email)
        subcriptor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
