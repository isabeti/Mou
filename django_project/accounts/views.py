from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.conf import settings
from django.contrib.auth.models import User

from .utils import get_tokens_for_user
from config.response import set_receive
from config.email_sender import send_new_email
from .tokens import account_activation_token
from profile_app.models import Profile

class Register(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        receive = set_receive(request, request.content_type)

        if receive.get('username') is None or receive.get('email') is None or receive.get('password') is None:
            return Response('The username, email and password is required.', status=400)

        elif User.objects.filter(username=receive.get('username'), is_active=True):
            return Response('The username already exists.', status=400)

        elif User.objects.filter(email=receive.get('email'), is_active=True):
            return Response('The email already exists.', status=400)
        
        User.objects.filter(email=receive.get('email'), is_active=False).delete()
        user = User.objects.create(username=receive.get('username'), email=receive.get('email'), is_active=False)
        user.set_password(receive.get('password'))

        email_subject =  'Account verification'
        email_content = '{site_url}activate-account/{uidb64}/{token}'.format(
            uidb64=urlsafe_base64_encode(force_bytes(user.pk)), token=account_activation_token.make_token(user), email=receive.get('email'), site_url=settings.SITE_URL
            
        )
        destination_email = receive.get('email')
        send_email = send_new_email(email_subject, email_content, destination_email)

        return Response('The email was sent successfully.', status=201)


class ActivateRegister(APIView):
    permission_classes = [AllowAny]

    def get(request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()

            create_obj = Profile.objects.create(user=user)
            return Response('The account verified successfully.', status=202)
        
        else:
            return Response(status=403)


class Login(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        receive = set_receive(request, request.content_type)

        if receive.get('username') is None or receive.get('password') is None:
            return Response('The username and passwor fields is required.', status=400)

        user = User.objects.filter(username=receive.get('username')).first() if '@' not in receive.get('username') else User.objects.get(email=receive.get('username')).first()
        if user is None:
            return Response('wrong username', status=400)
        
        if not user.check_password(receive.get('password')):
            return Response('wrong password', status=400)

        access_token = get_tokens_for_user(user)['access']
        refresh_token = get_tokens_for_user(user)['refresh']

        return Response({'access_token': access_token, 'refresh_token': refresh_token})


class ForgetPw(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        receive = set_receive(request, request.content_type)

        if receive.get('email') is None:
            return Response('The email field is required.', status=401)
        

        elif not User.objects.filter(email=receive.get('email')):
            return Response('The email does not exist.', status=401)
        
        user = User.objects.get(email=receive.get('email'))
        email_subject =  'Forget password'
        email_content = '{site_url}activate/forget-password/{uidb64}/{token}'.format(
            uidb64=urlsafe_base64_encode(force_bytes(user.pk)), token=account_activation_token.make_token(user), email=receive.get('email'), site_url=settings.SITE_URL
            
        )
        destination_email = receive.get('email')
        send_email = send_new_email(email_subject, email_content, destination_email)

        return Response('The email was sent successfully.', status=200)

class ActivateForgetPw(APIView):
    permission_classes = [AllowAny]

    def get(request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            return Response(status=202)
        
        else:
            return Response(status=403)

class ChangePw(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        receive = set_receive(request, request.content_type)

        if receive.get('email') is None or receive.get('password') is None:
            return Response('This email and password field is required.', status=401)
        
        user = get_object_or_404(User, email=receive.get('email'))
        user.set_password(receive.get('password'))
        user.save()
        return Response('The password was changed successfully.')