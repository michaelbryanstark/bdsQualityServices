from . import views 
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('certifications/', views.CertificationsView.as_view(), name='certifications'),
    path('services/', views.ServicesView.as_view(), name='services'),
]