from django.urls import path

from .views import CuantoCreateView, CuantoDetailView, CuantoListView, CuantoDeleteView, CuantoUpdateView

urlpatterns = [
    path('create/', CuantoCreateView.as_view(), name='create'),
    path('detail/<str:pk>', CuantoDetailView.as_view(), name='detail'),
    path('', CuantoListView.as_view(), name='list'),
    path('delete/<str:pk>/', CuantoDeleteView.as_view(), name='delete'),
    path('update/<str:pk>/', CuantoUpdateView.as_view(), name='update'),
]
