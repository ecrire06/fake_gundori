from django.urls import path
from fake_gundori import views
from .views import SoldierListView, SoldierCreateView, SoldierDetailView, SoldierUpdateView, SoldierDeleteView

urlpatterns = [
    path('soldier/list', views.SoldierListView.as_view(), name='soldier-list'),
    path('soldier/add', views.SoldierCreateView.as_view(), name='soldier-add'),
    path('soldier/<int:pk>', views.SoldierDetailView.as_view(), name='soldier_detail'),
    path('soldier/<int:pk>/update/', views.SoldierUpdateView.as_view(), name='soldier_update'),
    path('soldier/<int:pk>/delete/', views.SoldierDeleteView.as_view(), name='soldier-delete'),

    path('', views.index, name="index"),
    path('addsoldier/', views.addsoldier, name="addsoldier"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('detail/<int:id>', views.detail, name='detail'),
]
