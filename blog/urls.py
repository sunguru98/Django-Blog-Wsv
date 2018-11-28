from django.urls import path, include
from . import views

app_name = 'blog_app'
urlpatterns = [
    path("", views.IndexPageTemplateView.as_view(), name="home"),
    path("posts/", views.BlogPostListView.as_view(), name="blog_list"),
    path("post/<int:pk>/", views.BlogPostDetailView.as_view(), name="blog_detail"),
    path("post/create/", views.BlogPostCreateView.as_view(), name="blog_create"),
    path("post/edit/<int:pk>/", views.BlogPostEditView.as_view(), name="blog_update"),
    path("post/delete/<int:pk>/", views.BlogPostDeleteView.as_view(), name="blog_delete")
]