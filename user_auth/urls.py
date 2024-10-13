from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, HomePage,CustomLoginView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]