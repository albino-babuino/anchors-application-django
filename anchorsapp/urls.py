from django.urls import path
from .views import Index, CategoryDetail

urlpatterns = [
        path('', Index.as_view(), name='index'),
        path('category-detail/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
]
