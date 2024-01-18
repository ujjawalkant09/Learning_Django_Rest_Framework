from django.shortcuts import render
from .serializer import SignUpSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import User
from .tokens import create_jwt_pair_for_user
# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = []
    def post(self,request:Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            
            response = {
                "message":"User Created Successfully",
                "data":serializer.data
            }
             
            return Response(data=response,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = []
    def post(self,request:Request):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        print("email -",email," password ",password)
        if email and password:
            user = authenticate(email=email, password=password)
            print(user)
            if user:
                tokens = create_jwt_pair_for_user(user)
                response = {
                    "message":"Login successfull",
                    "token":tokens
                }
                return Response(data=response,status=status.HTTP_200_OK)
            else:
                return Response(data={"message":"Invalid email or password"})
        else:
            return Response(data={"message":"Email or Password is missing"})



    def get(self, request:Request):
        content={
            "user": str(request.user),
            "auth": str(request.auth)
        }

        return Response(data=content, status=status.HTTP_200_OK)


class AllUserDetails(APIView):
    permission_classes = []
    def post(self,request:Request):
        user = User.objects.all()
        return Response(data={"Count_Of_User":len(user)})