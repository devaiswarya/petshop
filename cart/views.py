from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import CartSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Cart

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_cartproduct(request):
    data=request.data.copy()
    data['user']=request.user.id
    serializer=CartSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'product added to cart successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_userproduct(request):
    value=Cart.objects.filter(user=request.user)
    result=CartSerializer(value,many=True)
    return Response({'message':'Product fetch successfully','data':result.data},status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_cart(request,pk):
    action=request.data.get('action')
    cart=Cart.objects.get(pk=pk,user=request.user.id)
    if action=="increase":
        cart.quantity+=1
    elif action == "decrease":
        if cart.quantity > 1:
            cart.quantity -=1
    cart.save()
    serializer=CartSerializer(cart)
    return Response({'messsage':'Cart Updated Successfully','data':serializer.data},status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_cartproduct(request,pk):
    value=Cart.objects.get(pk=pk,user=request.user.id)
    value.delete()
    return Response({'message':'Cart product deleted successfully'},status=status.HTTP_204_NO_CONTENT)

