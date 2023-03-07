from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('america/', include('america.urls')),
    path('europa/', include('europa.urls')),
]
