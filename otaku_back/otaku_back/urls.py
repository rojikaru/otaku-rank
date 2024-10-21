"""
URL configuration for otaku_back project.

The `urlpatterns` list routes URLs to viewsets. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function viewsets
    1. Add an import:  from my_app import viewsets
    2. Add a URL to urlpatterns:  path('', viewsets.home, name='home')
Class-based viewsets
    1. Add an import:  from other_app.viewsets import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .env import ENVIRON
from .viewsets.demographic import DemographicViewSet
from .viewsets.genre import GenreViewSet
from .viewsets.review import AnimeReviewViewSet, MangaReviewViewSet
from .viewsets.title import AnimeViewSet, MangaViewSet
from .viewsets.user import UserViewSet

router = DefaultRouter()
router.register(r'demographic', DemographicViewSet, basename='demographic')
router.register(r'user', UserViewSet, basename='user')
router.register(r'anime', AnimeViewSet, basename='anime')
router.register(r'manga', MangaViewSet, basename='manga')
router.register(r'genre', GenreViewSet, basename='genre')
router.register(r'review/anime', AnimeReviewViewSet, basename='anime_review')
router.register(r'review/manga', MangaReviewViewSet, basename='manga_review')

# The `urlpatterns` list routes URLs to viewsets.
urlpatterns = [
    path('api/', include(router.urls)),
]

if ENVIRON('DEBUG'):
    print('DEBUG MODE ENABLED')
    urlpatterns.append(path('admin/', admin.site.urls))