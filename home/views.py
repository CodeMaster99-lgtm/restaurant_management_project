from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from .models import menu_item
from .serializers import MenuItemSerializer
from django.db import DatabaseError

class MenuItemView(APIView):
    def get(self, request):
        try:
            items = MenuItem.objects.all()
            serializer = MenuItemSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except DatabaseError as e:
            {"error": "Database error occurred while fetching menu item."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR

    def post(self, request):
        try:
            serializer = MenuItemSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except DatabaseError as e:
            return Response(
                {"error": "Database error occured while adding a new menu item."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    def put(self, request, pk=None):
        try:
            item = MenuItem.objects.get(pk=pk)
            serializer = MenuItemSerializer(item , data=requeat.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except MenuItem.DoesNotExist:
            return Response(
                {"error": "Menu item not found."}
                status=status.HTTP_404_not_found
            )

        except DatabaseError:
            return Response(
                {"error": "Dtabase error occured while updating menu item."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    def delete(self, request, pk=None):

        try:
            item = MenuItem.objects.get(pk=pk)
            item.delete()
            return Response(
                {"message":"Menu item deleted successfully."},
                status=status.HTTP_204_NO_CONTENT
            )
        except DatabaseError:
            return Response(
                {"error": "Menu item not found."},
                status=status.HTTP_404_not_found
            )
        except DatabaseError:
            return Response(
                {"error": "Database error occured while deleting menu item."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )