from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Index, CategoryDetail, RegisterView


urlpatterns = [
        path('login/', auth_views.LoginView.as_view(template_name='anchorsapp/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Ruta para logout
        path('register/', RegisterView.as_view(), name='register'),
        path('', Index.as_view(), name='index'),
        path('category-detail/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
]



