from . import views
from django.urls import path

urlpatterns = [
    path("homepage/", views.home, name="post_home"),
    path("", views.PostListCreateView.as_view(), name="list_posts"),
    path("<int:pk>/", views.PostRetriveUpdateDelete.as_view(), name="post_details"),
]