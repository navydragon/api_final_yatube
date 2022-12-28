from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('v1/posts', PostViewSet, basename='posts')
router.register('v1/groups', GroupViewSet, basename='groups')
router.register('v1/follow', FollowViewSet, basename='follow')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
