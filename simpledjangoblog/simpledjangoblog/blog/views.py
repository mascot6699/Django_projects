from django.shortcuts import render
from . import serializers
from . import models

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Post(APIView):


    def get(self, request, post_id, format=None):

        """
        GET post api
        """
        try:
            post = models.Post.objects.get(id = post_id)
            serializer = serializers.PostSerializer(post)
            if serializer.is_valid:
                if serializer.is_valid:
                    return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print e
            return Response({"status":"error"}, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request, format=None):
        """
        post post api
        """
        serializer = serializers.PostSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)