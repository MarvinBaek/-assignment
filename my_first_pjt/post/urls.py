from django.urls import path
from .views import post_list, post_detail
from .views import post_list, post_detail, PostCreateView
from .views import PostListView
from .views import PostUpdateView, post_detail
from .views import PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),  # PostListView 사용
    path('post/<int:pk>/', post_detail, name='post_detail'),  # 게시글 상세 페이지
    path('post/create/', PostCreateView.as_view(), name='post_create'),  # 새 게시글 작성
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),  # 수정 URL
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # 삭제 URL
]
