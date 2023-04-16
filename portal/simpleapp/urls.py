from django.urls import path
from .views import PostList, PostDetail, NewsCreate, ArticleCreate, PostUpdate, PostDelete


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('articles/create/', ArticleCreate.as_view(), name='article_create'),
   path('news/<int:pk>/update/', PostUpdate.as_view(), name='news_update'),
   path('articles/<int:pk>/update/', PostUpdate.as_view(), name='article_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='article_delete'),
]