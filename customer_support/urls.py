from django.urls import path
from . import views

app_name = 'customer_support'

urlpatterns = [
    path('dashboard/', views.support_dashboard, name='dashboard'),
    # path('requests/', views.update_request_status, name='request_list'),
    path('requests/<int:request_id>/', views.request_detail, name='request_detail'),
     path('requests/<int:service_request_id>/update/', views.update_request_status, name='update_status'),
]
  