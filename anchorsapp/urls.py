from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Categories, CategoryDetail, RegisterView, HomePage


urlpatterns = [
        path('', HomePage.as_view(), name='home'),  # Página de inicio
        path('login/', auth_views.LoginView.as_view(template_name='anchorsapp/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('register/', RegisterView.as_view(), name='register'),
        path('categories/', Categories.as_view(), name='categories'),  # Cambiamos la URL de las categorías a /categories
        path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),  # Cambiamos el detail a /categories/<pk>
]



