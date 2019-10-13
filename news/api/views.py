from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from news.models import Article
from news.api.serializers import ArticleSerializer


@api_view(["GET","POST"])
def article_list_create_api_view(request):
    
    if request.method == "GET":
        articles = Article.objects.filter(active=True)
        sertializer = ArticleSerializer(articles, many=True)
        return Response(sertializer.data)

    elif request.method == "POST":
        sertializer = ArticleSerializer(data=request.data)
        if sertializer.is_valid():
            sertializer.save()
            return Response(sertializer.data, status=status.HTTP_201_CREATED)
        return Response(sertializer.errors, status=status.HTTP_400_BAD_REQUEST)