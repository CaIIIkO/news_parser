from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from applications.views import NewsViewSet


urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('news/last', NewsViewSet.as_view({'get': 'get_new_news'}), name='docs'),
    path('news/random', NewsViewSet.as_view({'get': 'get_random_news'}), name='docs'),
    path('news/', NewsViewSet.as_view({'get': 'get_news_by_day'}), name='docs'),
    path('news/<str:category>', NewsViewSet.as_view({'get': 'get_news_day_by_category'}), name='docs'),
]
