from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemsSerializer
from rest_framework.response import Response
from django.core.mail import send_mail



class OrderItemView(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemsSerializer
    permission_class = [permissions.IsAuthenticated,]


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_class = [permissions.IsAuthenticated,]

    def get_queryset(self):
        print(self.request.user)
        if self.request.user.is_authenticated:
            return self.queryset.filter(owner=self.request.user)
        return []


    def create(self, request):
        print(request.data.items)
        # created = Order.objects.create(owner=request.user, items=request.data.items)
        send_mail(
            'request.data[]',
            'request.data.items',
            'info@kz.kz',
            ['aqarys080@gmail.com'],
            fail_silently=False,
        )
        return Response({'message': 'ok'})
        # return Response(created)

