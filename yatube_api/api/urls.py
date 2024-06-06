from posts.views import PostViewSet, GroupViewSet, CommentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)

post_router = DefaultRouter()
post_router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_id>/', include(post_router.urls))
]
