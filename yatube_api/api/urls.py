from posts.views import PostViewSet, GroupViewSet, CommentViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)


comment_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

comment_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/posts/<int:post_id>/comments/', comment_list,
         name='comment-list'),
    path('api/v1/posts/<int:post_id>/comments/<int:pk>/', comment_detail,
         name='comment-detail'),
]
