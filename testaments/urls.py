from django.urls import path
from .views import (
    TestamentListView,
    TestamentUpdateView,
    TestamentDetailView,
    TestamentDeleteView,
    TestamentCreateView,)

urlpatterns = [
    path(
        '<int:pk>/edit/',
        TestamentUpdateView.as_view(),
        name='testament_edit'),
    path(
        '<int:pk>/',
        TestamentDetailView.as_view(),
        name='testament_detail'),
    path(
        '<int:pk>/delete/',
        TestamentDeleteView.as_view(),
        name='testament_delete'),
    path('add/', TestamentCreateView.as_view(), name='testament_add'),
    path('', TestamentListView.as_view(), name='testament_list'),
]
