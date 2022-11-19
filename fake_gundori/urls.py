from django.urls import path
from fake_gundori import views

urlpatterns = [
    path('', views.index, name="index"),
    path('addsoldier/', views.addsoldier, name="addsoldier"),
]
