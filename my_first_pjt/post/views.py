
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView
from django.conf import settings
from django.http import HttpResponseForbidden
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # 최신 게시글부터 표시
    return render(request, 'post/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # 게시글 작성 시 필요한 필드
    template_name = 'post/post_form.html'
    login_url = '/login/'  # 로그인 페이지 URL 설정 (로그인 안 되어 있으면 이 페이지로 리다이렉트)

    def form_valid(self, form):
        # 로그인한 사용자만 작성자로 설정
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # 게시글 작성 후 해당 게시글 상세 페이지로 리다이렉트
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    

class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'  # 게시글 목록을 템플릿에서 'posts'로 사용

    # 로그인하지 않으면 '/login/' 페이지로 리다이렉트
    login_url = '/login/'  


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']  # 수정할 필드
    template_name = 'post/post_form.html'

    def get_success_url(self):
        # 게시글 수정 후 상세 페이지로 리다이렉트
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    context_object_name = 'post'

    def get_success_url(self):
        # 게시글 삭제 후 게시글 목록 페이지로 리다이렉트
        return reverse_lazy('post_list')