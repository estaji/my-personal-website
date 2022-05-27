from django.urls import path
from .views import BlogView, ArticleView


app_name = "blog"
urlpatterns = [
    path(
        '',
        BlogView.as_view(template_name="blog/home.html"),
        name='blog',
    ),
    path(
        'article/',
        ArticleView.as_view(template_name="blog/article.html"),
        name='article',
    ),
]