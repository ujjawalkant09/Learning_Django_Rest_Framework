from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status, generics,mixins
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

class PostListCreateView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    """
    A view for creating and listing posts
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

        
class PostRetriveUpdateDelete(generics.GenericAPIView, 
                              mixins.RetrieveModelMixin, 
                              mixins.UpdateModelMixin, 
                              mixins.DestroyModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    
    def put(self, request:Request, *args, **kwargs):
        return self.update(request,*args, **kwargs)
    
    def delete(self,request:Request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
         
    