from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import ArticleSerializer
from .models import Article
from django.views.decorators.csrf import csrf_exempt

# REST Framework api_view() Decorator  Start
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# REST Framework api_view() Decorator  End


# class based api views start
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# end

# REST Generic Views & Mixins Start
from rest_framework import generics
from rest_framework import mixins


# REST Generic Views & Mixins end
# Create your views here.



# REST Framework Function Based API Views Start
# @csrf_exempt
# def article_list(request):
#     if request.method =='GET':
#         articles=Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return JsonResponse(serializer.data,safe=False)

#     elif request.method =='POST':
#         data = JSONParser().parse(request)
#         serializer=ArticleSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors,status=400)

# @csrf_exempt
# def article_detail(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method =='GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer=ArticleSerializer(article,data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors,status=400)

#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)

# REST Framework Function Based API Views End


# REST Framework api_view() Decorator  Start

@api_view(['GET','POST'])
def article_list(request):
    if request.method =='GET':
        articles=Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method =='POST':
        serializer=ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
       
        serializer=ArticleSerializer(article,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# REST Framework api_view() Decorator  End


#Class Based API Views

class ArticleAPIView(APIView):
    def get(self,request):
        articles=Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
 
    def get_object(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
 
    def get(self, request, id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
 
 
 
    def put(self, request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# end class based views


# REST Generic Views & Mixins   Start

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,mixins.UpdateModelMixin, mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
 
  
 
    def get(self, request, id = None):
 
        if id:
            return self.retrieve(request)
 
        else:
           return self.list(request)
 
    def post(self, request):
        return self.create(request)
 
    def put(self, request, id=None):
        return self.update(request, id)
 
    def delete(self, request, id):
        return self.destroy(request, id)

# REST Generic Views & Mixins    End