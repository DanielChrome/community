from django.urls import path
from .views import SignUpView, MyLoginView
from .forms import CustomUserLoginForm
from django.contrib.auth import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout')
]

# path('login/', views.LoginView.as_view(authentication_form=CustomUserLoginForm), name='login'),
