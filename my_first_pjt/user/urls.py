
from django.urls import path
from .views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView
from .views import SignUpView, user_profile, delete_account

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', user_profile, name='user_profile'),  # 프로필 페이지 URL 추가
    path('update/', user_profile, name='update'),
    path('delete/', delete_account, name='delete'),
]
