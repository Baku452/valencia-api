from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

# from .models import ContactUs, Newsletter
from .serializers import ContactUsSerializer, NewsletterSerializer

subject = 'Welcome to Valencia Travel'
html_message = render_to_string('mail_template.html', {'context': 'values'})
plain_message = strip_tags(html_message)
from_email = 'From <michel.hinostroza@gmail.com>'
to = 'michel.hinostroza@gmail.com'


class ContactCreateApi(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            send_mail(subject, plain_message, from_email, [to], html_message=html_message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsletterCreateApi(APIView):
    def post(self, request):
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
