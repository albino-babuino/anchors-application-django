from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, HomePage


urlpatterns = [
    path('', HomePage.as_view(), name='home'),  # Página de inicio
    path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]



