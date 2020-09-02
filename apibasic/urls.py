from django.urls import path,include
from .views import article_list,article_detail,ArticleAPIView,ArticleDetails,GenericAPIView

# REST Framework Viewsets & Routers
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')


# REST Framework Viewsets & Routers

urlpatterns = [
    # REST Framework api_view() Decorator
    # path('article/',article_list),
    #  path('detail/<int:pk>/',article_detail),

    #Class Based API Views
    path('article/',ArticleAPIView.as_view()),
    path('detail/<int:id>/',ArticleDetails.as_view()),
    
    # REST Generic Views & Mixins  
    path('generic/article/<int:id>/', GenericAPIView.as_view()),

   # REST Framework Viewsets & Routers
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls))
    # REST Framework Viewsets & Routers
    
   
]