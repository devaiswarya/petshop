from rest_framework.decorators import api_view
from .serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Products

@api_view(['POST'])
def create_product(request):
    serilaizer=ProductSerializer(data=request.data)
    if serilaizer.is_valid():
        serilaizer.save()
        return Response({'message':'product created successfully','data':serilaizer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serilaizer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def fetch_product(request):
    value=Products.objects.all()
    result=ProductSerializer(value,many=True,context={'request':request})
    return Response({'message':'product fetched successfully','data':result.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request):
    category_id=request.query_params.get('category_id')
    value=Products.objects.all()
    if category_id:
        value=value.filter(category_id=category_id)
    result=ProductSerializer(value,many=True,context={'request':request})
    return Response({'message':'product fetched successfully','data':result.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def product_one(request,pk):
    value=Products.objects.get(pk=pk)
    result=ProductSerializer(value,context={'request':request})
    return Response({'message':'product fetched successfully','data':result.data},status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_product(request,pk):
    value=Products.objects.get(pk=pk)
    serializer=ProductSerializer(value,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'product updated successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_product(request,pk):
    value=Products.objects.get(pk=pk)
    value.delete()
    return Response({'message':'product deleted successfully'},status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def new_arrival(request):
    value=Products.objects.order_by('-created_at')[:4]
    serializer=ProductSerializer(value,many=True,context={'request':request})
    return Response({'message':'New Arrival fetched successfully','data':serializer.data},status=status.HTTP_200_OK)
