from django.urls import path
from . import views
app_name = 'customer_portal' 
urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('service_history/', views.service_history, name='service_history'),
    path('service-request/', views.service_request_form, name='service_request_form'),
    path('service-request-success/', views.service_request_success, name='service_request_success'),
    path('track-request/<int:request_id>/', views.track_request, name='track_request'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.view_profile, name='profile'),
]
