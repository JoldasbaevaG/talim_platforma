from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('boshlash/', views.boshlash, name='boshlash'),
    path('registratsiya/', views.registratsiya, name='registratsiya'),
    path('tashkilot/', views.tashkilot, name='tashkilot'),
    path('yordam/', views.yordam, name='yordam'),
    path('kabinet/', views.kabinet, name='kabinet'),
]
