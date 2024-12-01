from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/create/', views.contact_create, name='contact_create'),
    path('contact/edit/<int:pk>/', views.contact_edit, name='contact_edit'),
    path('contact/delete/<int:pk>/', views.contact_delete, name='contact_delete'),
]
