from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from applications.services.news_service import NewsService
from drf_spectacular.utils import OpenApiParameter, extend_schema
class NewsViewSet(ViewSet):
    news_service = NewsService()
    
    @extend_schema(
    summary='Get news by day',
    parameters=[
        OpenApiParameter(
            name='year',
            type=int,
            location=OpenApiParameter.QUERY,
            required=True,
            description='Year'
        ),
        OpenApiParameter(
            name='month',
            type=int,
            location=OpenApiParameter.QUERY,
            required=True,
            description='Month'
        ),
        OpenApiParameter(
            name='day',
            type=int,
            location=OpenApiParameter.QUERY,
            required=True,
            description='Day'
        ),
        OpenApiParameter(
            name='quantity',
            type=int,
            location=OpenApiParameter.QUERY,
            required=True,
            description='Number of news items'
        )
    ]
    )
    def get_news_by_day(self, request):
        quantity = int(request.GET.get('quantity'))
        day = request.GET.get('day')
        month = request.GET.get('month')
        year = request.GET.get('year')
        news = self.news_service.get_news_day(quantity, year, month, day)
        news_data = [
            {
                'text': news_item.text,
                'link': news_item.link,
                'time': news_item.time,
                'category': news_item.category
            } for news_item in news
        ]
        response_data = {
            'news': news_data
        }
        return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})
    
    @extend_schema(
    summary='Get news by day and category',
    parameters=[
        OpenApiParameter(
            name='year',
            type=str,
            location=OpenApiParameter.QUERY,
            required=False,
            default='2024',
            description='Year'
        ),
        OpenApiParameter(
            name='month',
            type=str,
            location=OpenApiParameter.QUERY,
            required=False,
            default='01',
            description='Month'
        ),
        OpenApiParameter(
            name='day',
            type=str,
            location=OpenApiParameter.QUERY,
            required=False,
            default='01',
            description='Day'
        ),
        OpenApiParameter(
            name='quantity',
            type=int,
            location=OpenApiParameter.QUERY,
            required=False,
            default=10,
            description='Number of news items'
        )
    ]
    )
    def get_news_day_by_category(self, request, category):
        quantity = int(request.GET.get('quantity', 10))
        year = request.GET.get('year', '2024')
        month = request.GET.get('month', '01')
        day = request.GET.get('day', '01')

        news = self.news_service.get_news_day_by_category(quantity, year, month, day, category)
        news_data = [
            {
                'text': news_item.text,
                'link': news_item.link,
                'time': news_item.time,
                'category': news_item.category
            } for news_item in news
        ]
        print(112)
        response_data = {
            'news': news_data
        }
        return JsonResponse(response_data, json_dumps_params={'ensure_ascii': False})
    
    
    @extend_schema(
    summary='Get the latest news'
    )
    def get_new_news(self, request):
        new_news = self.news_service.get_new_news()
        news_data = {
            'text': new_news.text,
            'link': new_news.link,
            'time': new_news.time,
            'category': new_news.category
        }
        return JsonResponse(news_data)
    
    @extend_schema(
    summary='Get a random news item'
    )
    def get_random_news(self, request):
        random_news = self.news_service.get_random_news()
        news_data = {
            'text': random_news.text,
            'link': random_news.link,
            'time': random_news.time,
            'category': random_news.category
        }
        return JsonResponse(news_data)