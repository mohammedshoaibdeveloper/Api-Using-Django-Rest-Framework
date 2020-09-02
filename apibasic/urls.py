from django.urls import path
from .views import article_list,article_detail,ArticleAPIView,ArticleDetails

urlpatterns = [
    # REST Framework api_view() Decorator
    # path('article/',article_list),
    #  path('detail/<int:pk>/',article_detail),

    #Class Based API Views
    path('article/',ArticleAPIView.as_view()),
    path('detail/<int:id>/',ArticleDetails.as_view()),
    
   
]