from django.shortcuts import render
from django.views import generic, View
from .models import Info

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_Info_list'

    def get_queryset(self):
        
        return Info.objects.order_by('updated_on')[:5]
    
class ContactView(generic.ListView):
    template_name = 'contact.html'
    context_object_name = 'latest_Info_list'

    def get_queryset(self):
        
        return Info.objects.order_by('updated_on')[:5]
    
class CertificationsView(generic.ListView):
    template_name = 'certifications.html'
    context_object_name = 'latest_Info_list'

    def get_queryset(self):
        
        return Info.objects.order_by('updated_on')[:5]
    
class ServicesView(generic.ListView):
    template_name = 'services.html'
    context_object_name = 'latest_Info_list'

    def get_queryset(self):
        
        return Info.objects.order_by('updated_on')[:5]