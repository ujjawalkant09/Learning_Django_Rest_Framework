from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, APIView
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

class PostListCreateView(APIView):
    """
    A view for creating and listing posts
    """
    serializer_class = PostSerializer
    
    def get(self,request:Request,*args,**kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request:Request,*args,**kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message ": "Post Created",
                "data ": serializer.data
            }
            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
        
class PostRetriveUpdateDelete(APIView):
    serliazer_class = PostSerializer
    def get(self,request:Request,post_id:int):
        post = get_object_or_404(Post,pk=post_id)
        serliazer = self.serliazer_class(post)
        response = {
            "message":"Post",
            "data":serliazer.data
        }
        return Response(data=response,status=status.HTTP_200_OK)

    def put(self,request:Request,post_id:int):
        post = get_object_or_404(Post,pk=post_id)
        data = request.data
        serializer = self.serliazer_class(instance=post,data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Message ": "Post Updated Sucessfully ",
                "data" : data
            }
            return Response(data=response,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request:Request,post_id:int):
        post = get_object_or_404(Post,pk=post_id)
        post.delete()
        response = {
            "message ":"Post has been deleted"
        }
        return Response(data=response,status=status.HTTP_204_NO_CONTENT)
