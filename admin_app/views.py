from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
import jwt
import json

from .serializers import UserSerializer
from admin_proj.settings import SECRET_KEY

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CreateUser(CreateAPIView):
    serializer_class = UserSerializer
    model=User()
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            user = self.model.__class__.objects.get(username=serializer.data['username'])
            payload = jwt_payload_handler(user)
            return Response({
                'response_code':'success',
                'response_msg':'User registered successfully',
                'username':user.username,
                'token': jwt.encode(payload, SECRET_KEY)
                },status.HTTP_200_OK)
        else:
            return Response(
              {'response_code':'error',
                'response_msg':serializer.errors},status.HTTP_400_BAD_REQUEST
            )


class LoginUser(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            payload = jwt_payload_handler(user)            
            return Response({
                'response_code':'success',
                'response_msg':'Login successfull',
                'username':user.username,
                'token': jwt.encode(payload, SECRET_KEY)
                },status.HTTP_200_OK)
        else:
            return Response(
              {'response_code':'error',
                'response_msg':'Invalid credentials'},status.HTTP_400_BAD_REQUEST
            )


class DashboardDetail(APIView):
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        data={'comments':5,
              'tasks':2,
              'orders':1,
              'tickets':3,
        }
        return Response({
                'response_code':'success',
                'response_msg':'Dashboard details',
                'data':data
                },status.HTTP_200_OK)
