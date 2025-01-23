from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

class SignUpView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'user/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            # 새 사용자 저장
            new_user = form.save()
            # 자동 로그인 처리
            login(request, new_user)
            # 로그인 후 게시물 목록 페이지로 리다이렉트
            return redirect('post_list')  # 'post_list'는 게시물 목록 페이지 URL
        return render(request, 'user/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        # 로그인 성공 후 게시물 목록 페이지로 이동
        return redirect('post_list').url


class CustomLogoutView(LogoutView):
    template_name = 'user/logout.html'  # 로그아웃 페이지가 필요하면 템플릿 추가



@login_required
def user_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')  # 프로필 페이지로 리다이렉트
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'user/profile.html', {'form': form})

@login_required
def delete_account(request):
    # 구현 코드
    return render(request, 'user/delete.html')