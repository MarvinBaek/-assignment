
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'profile_image', 'bio')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()  # CustomUser 모델을 사용
        fields = ['username', 'email', 'profile_image', 'bio']  # 필요에 따라 추가/수정

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['password1', 'password2']