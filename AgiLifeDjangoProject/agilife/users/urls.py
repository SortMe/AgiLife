from django.conf.urls import include
from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fullcalendar/', views.fullcalendar, name='fullcalendar'),
    url(r'^schedule/', include('schedule.urls')), 
    
]
