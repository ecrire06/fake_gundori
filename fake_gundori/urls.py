from django.urls import path
from fake_gundori import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('add/addrecord/', views.addrecord, name="addrecord"),
]
