from rest_framework.decorators import api_view
from .serializer import CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Category

@api_view(['POST'])
def create_category(request):
    serializer=CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Category Created Successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetch_category(reqeust):
    value=Category.objects.all()
    result=CategorySerializer(value,many=True)
    return Response({'message':'category fetched successfully','data':result.data},status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_category(request,pk):
    value=Category.objects.get(pk=pk)
    serializer=CategorySerializer(value,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'messgae':'Category Updated Successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_category(request,pk):
    value=Category.objects.get(pk=pk)
    value.delete()
    return Response({'message':'Category Deleted Successfully'})