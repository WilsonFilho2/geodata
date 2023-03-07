from django.urls import path
from . import views

urlpatterns = [
    path('', views.europa, name='europa'),
    path('alemanha/', views.alemanha, name='alemanha'),
    path('italia/', views.italia, name='italia'),
    path('franca/', views.franca, name='franca'),
]

