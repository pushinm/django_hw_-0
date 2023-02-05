from django.urls import path
from .views import article_view, change_article, delete_article

app_name = 'magazine'

urlpatterns = [
    path('', article_view, name='article_view'),
    path('change/', change_article, name='change_article'),
    path('delete/', delete_article, name='delete_article'),
    path('<int:pk>/', article_view, name='article_view'),
]