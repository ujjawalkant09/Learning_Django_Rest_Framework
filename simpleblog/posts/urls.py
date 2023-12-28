from . import views
from django.urls import path

urlpatterns = [
    path("homepage/", views.home, name="post_home"),
    path("", views.PostListCreateView.as_view(), name="list_posts"),
    path("<int:post_id>/", views.PostRetriveUpdateDelete.as_view(), name="PRUD"),
]