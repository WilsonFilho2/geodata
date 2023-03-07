from django.urls import path
from . import views

urlpatterns = [
    path('', views.america, name='america'),
    path('brasil/', views.brasil, name='brasil'),
    path('argentina/', views.argentina, name='argentina')
]
