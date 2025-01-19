from django.contrib import admin

# Register your models here.
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.support_dashboard, name='support_dashboard'),
    path('request/<int:request_id>/', views.request_detail, name='request_detail'),
    path('request/<int:request_id>/update_status/<str:new_status>/', views.update_request_status, name='update_request_status'),
]
