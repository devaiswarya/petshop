from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializer import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from cart.models import Cart
from orderitem.models import OrderItem

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    user=request.user
    cartItems=Cart.objects.filter(user=user)
    if not cartItems.exists():
        return Response({'message':'Cart is empty'},status=status.HTTP_400_BAD_REQUEST)
    total_amount=0
    for item in cartItems:
        total_amount += item.product.price*item.quantity
    data={
        'user':user.id,
        'total_amount':total_amount
    }
    serializer=OrderSerializer(data=data)
    if serializer.is_valid():
        order=serializer.save()
        for item in cartItems:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            item.product.stock-=item.quantity
            item.product.save()
            cartItems.delete()
        return Response({'message':'Order created successfully','data':serializer.data},status=status.HTTP_201_CREATED)
    return Response({'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def fetch_order(request):
    order=Order.objects.filter(user=request.user.id)
    serializer=OrderSerializer(order,many=True)
    return Response({'message':'order fetched successfullly','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_detail(request,pk):
    order=Order.objects.get(pk=pk,user=request.user)
    select=OrderItem.objects.filter(order=order)
    serializer=OrderSerializer(select,many=True)
    return Response({'message':'orderitem fetch sucessfully','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_order(request,pk):
    order=Order.objects.get(pk=pk,user=request.user)
    if order.status=="Shipped":
        return Response({'message':'order cannot be cancelled'},status=status.HTTP_400_BAD_REQUEST)
    if order.status=="Delivered":
        return Response({'message':'order cannot be cancelled'},status=status.HTTP_400_BAD_REQUEST)
    if order.status=="Cancelled":
        return Response({'message':'order already cancelled'},status=status.HTTP_400_BAD_REQUEST)
    order.status="Cancelled"
    order.save()
    order_items=OrderItem.objects.filter(order=order)
    for item in order_items:
        item.product.stock+=item.quantity
        item.product.save()
    return Response({'message':'order updated sucessfully'},status=status.HTTP_201_CREATED)