from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Categories, CategoryDetail, RegisterView, HomePage,CreateCategory, CreateAnchor, DeleteCategory, DeleteAnchor, UpdateCategory, UpdateAnchor


urlpatterns = [
        path('', HomePage.as_view(), name='home'),  # Página de inicio
        path('login/', auth_views.LoginView.as_view(template_name='anchorsapp/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('register/', RegisterView.as_view(), name='register'),
        path('categories/', Categories.as_view(), name='categories'),  # Cambiamos la URL de las categorías a /categories
        path('categories/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),  # Cambiamos el detail a /categories/<pk>
        path('create-category/', CreateCategory.as_view(), name='create_category'),  # Vista para crear categoría
        path('create-anchor/<int:category_id>/', CreateAnchor.as_view(), name='create_anchor'),  # Vista para crear anclaje
        path('delete-category/<int:pk>/', DeleteCategory.as_view(), name='delete_category'),  # Vista para eliminar categoría
        path('delete-anchor/<int:pk>/', DeleteAnchor.as_view(), name='delete_anchor'),  # Vista para eliminar enlace
        path('update-category/<int:pk>/', UpdateCategory.as_view(), name='update_category'),  # Actualizar categoría
        path('update-anchor/<int:pk>/', UpdateAnchor.as_view(), name='update_anchor'),  # Actualizar enlace
]



