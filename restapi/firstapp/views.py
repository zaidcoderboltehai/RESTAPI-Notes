from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import User,Accounts
from .serializer import UserSerializer,AccountSerializer
from rest_framework.response import Response
from rest_framework import status

# class CreateUser(generics.CreateAPIView): 
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class GetUsers(generics.ListAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class GetCreateUsers(generics.ListCreateAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class GetUser(generics.RetrieveAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class Destroy(generics.DestroyAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class UpdateUser(generics.UpdateAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class GetDestroyUpdateUser(generics.RetrieveUpdateDestroyAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class GetCreateAccounts(generics.ListCreateAPIView):
#     queryset=Accounts.objects.all()
#     serializer_class=AccountSerializer

# class GetDestroyUpdateAccount(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Accounts.objects.all()
#     serializer_class=AccountSerializer

class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class AccountView(viewsets.ModelViewSet):
    queryset=Accounts.objects.all()
    serializer_class=AccountSerializer


