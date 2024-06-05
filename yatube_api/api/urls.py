from posts.views import PostViewSet, GroupViewSet, CommentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('comments', CommentViewSet, basename='comments')
router.register('groups', GroupViewSet)

urlpatterns = [
    path('', include(router.urls))
]
