from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,status
from rest_framework.request import Request
from rest_framework.response import Response
from posts.serializers import PostSerializer
from .models import Post
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action

from drf_yasg.utils import swagger_auto_schema
# Create your views here 

# class PostViewset(viewsets.ViewSet):
    # def list(self,request:Request):
    #     queryset = Post.objects.all()
    #     serializer = PostSerializer(instance=queryset,many=True)
    #     return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    # def retrieve(self,request:Request,pk=None):
    #     post = get_object_or_404(Post,pk=pk)
    #     serializer = PostSerializer(instance=post)
    #     return Response(data=serializer.data,status=status.HTTP_200_OK)
    
class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication,JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @swagger_auto_schema(
            operation_summary="List All Posts",
            operation_description="Return all the post that have in our database",
    )
    @action(detail=False, methods=['GET'])
    def get_all_count_post(self, request):
        """
        Custom action to retrieve all users.
        """
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response({"Total_Number_Of_Post": len(serializer.data)})