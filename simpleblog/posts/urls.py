from . import views
from django.urls import path

urlpatterns = [
    path("homepage/", views.home, name="post_home"),
    path("", views.list_post, name="list_posts"),
    path("<int:post_id>/",views.post_details, name="post_details"),
    path("update/<int:post_id>/",views.update_post, name="update_post"),
    path("delete/<int:post_id>/",views.delete_post, name="delete_post"),
    path("post_content/",views.post_content,name="post_content")
]