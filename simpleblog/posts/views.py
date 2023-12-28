from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
# Create your views here.
@api_view(http_method_names=['GET','POST'])
def home(request: Request):
    
    if request.method == "POST":
        data = request.data 
        response = {"messages":"Hello World","data":data}
        return Response(data=response,status=status.HTTP_201_CREATED)

    response = {"message": "Hello World"}
    return Response(data = response,status=status.HTTP_200_OK)


@api_view(http_method_names=["GET","POST"])
def list_post(request:Request):
    
    if request.method == "POST":
        data = request.data
        serilizer = PostSerializer(data=data)
        if serilizer.is_valid():
            serilizer.save()
            response = {
                "message": "Post has Been Created",
                "data": serilizer.data
            }
            return Response(data= response,status=status.HTTP_201_CREATED)
        return Response(data=serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    posts = Post.objects.all()
    serilizer = PostSerializer(instance=posts, many=True)
    response = {
        "message":"posts",
        "data":serilizer.data
    }
    return Response(data=response, status=status.HTTP_200_OK)

@api_view(http_method_names=["POST"])
def post_content(request:Request):
    data = request.data
    serilizer = PostSerializer(data=data)
    if serilizer.is_valid():
        serilizer.save()
        response = {
            "message": "Post has Been Created",
            "data": serilizer.data
        }
        return Response(data= response,status=status.HTTP_201_CREATED)
    return Response(data=serilizer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(http_method_names=["GET"])
def post_details(request:Request, post_id:int):
    post = get_object_or_404(Post,pk=post_id)
    serializer = PostSerializer(instance=post)
    response = {
        "message":"post",
        "data":serializer.data
    }

    return Response(data=response,status=status.HTTP_200_OK)
  
# @api_view(http_method_names=["GET"])
# def get_post_by_id(request:Request,post_id:int):
#     pass

@api_view(http_method_names=["PUT"])
def update_post(request:Request,post_id:int):
    post = get_object_or_404(Post,pk=post_id)
    data = request.data
    serializer = PostSerializer(instance=post,data=data)
    if serializer.is_valid():
        serializer.save()
        response = {
            "message":"Post Updated Successfully",
            "data":serializer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)
    return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


@api_view(http_method_names=["DELETE"])
def delete_post(request:Request,post_id:int):
    post = get_object_or_404(Post,pk=post_id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    