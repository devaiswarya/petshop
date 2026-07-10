from rest_framework.decorators import api_view
from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from django.contrib.auth.hashers import make_password,check_password
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def create_user(request):
    email=request.data.get('email')
    phone=request.data.get('phone')
    if not phone :
        return Response({'message':'Enter the phone number'},status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response({'message':'Email already exists'},status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(phone=phone).exists():
        return Response({'message':'Phone Number already exists'},status=status.HTTP_400_BAD_REQUEST)
    if len(phone)!=10:
        return Response({'message':'Enter the valid phone number'},status=status.HTTP_400_BAD_REQUEST)
    if not phone.isdigit():
        return Response({'message':'Enter the valid phone number'},status=status.HTTP_400_BAD_REQUEST)
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        v=make_password(request.data['password'])
        serializer.save(password=v)
        return Response({'message':'User created successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

   
@api_view(["POST"])
def login_user(request):
    username=request.data.get('username')
    password=request.data.get('password')
    if User.objects.filter(username=username).exists():
        value=User.objects.get(username=username)
        serializer=UserSerializer(value)
        if check_password(password,value.password):
            refresh=RefreshToken.for_user(value)
            return Response({'message':'Login successfully','refresh':str(refresh),'access':str(refresh.access_token)},status=status.HTTP_201_CREATED)
        return Response({'messgae':'Password Invalid'},status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'username does not exists'},status=status.HTTP_400_BAD_REQUEST)



    