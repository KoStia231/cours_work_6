from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import (
    BlogIndexView, BlogDetailView, BlogCreateView,
    BlogUpdateView, BlogDeleteView
)

app_name = BlogConfig.name

urlpatterns = [
                  path('', BlogIndexView.as_view(), name='index'),
                  path('detail/<slug:slug>/', cache_page(300)(BlogDetailView.as_view()), name='detail'),
                  path('update/<slug:slug>/', BlogUpdateView.as_view(), name='update'),
                  path('delete/<slug:slug>/', BlogDeleteView.as_view(), name='delete'),
                  path('create/', BlogCreateView.as_view(), name='create'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
