from .views import *
from django.urls import path

urlpatterns = [
    path('', AnonsListView.as_view(), name='anons_list'),
    path('<int:pk>/', AnonsDetailView.as_view(), name='anons_detail'),
    path('create/', AnonsCreateView.as_view(), name='anons_create'),
    path('delete/<int:pk>', AnonsDeleteView.as_view(), name='anons_delete'),
    path('update/<int:pk>', AnonsUpdateView.as_view(), name='anons_update'),
    path('like/<int:pk>', LikeView, name='like_post'),
]