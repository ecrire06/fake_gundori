from django.urls import path
from fake_gundori import views

urlpatterns = [
    path('', views.index, name="index"),
    path('soldiers/', views.SoldierListView.as_view(), name='soldiers'),
    path('soldier/<int:pk>', views.SoldierDetailView.as_view(), name='soldier_detail'),
    
    path('addsoldier/', views.addsoldier, name="addsoldier"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('detail/<int:id>', views.detail, name='detail'),
]
