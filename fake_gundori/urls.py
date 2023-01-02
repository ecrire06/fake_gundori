from django.urls import path
from fake_gundori import views
from .views import SoldierListView, SoldierCreateView, SoldierDetailView, SoldierUpdateView, SoldierDeleteView
from django.views.generic import RedirectView

urlpatterns = [
    path('soldier/', views.SoldierListView.as_view(), name='soldier-list'),
    path('soldier/add', views.SoldierCreateView.as_view(), name='soldier-add'),
    path('soldier/<int:pk>', views.SoldierDetailView.as_view(), name='soldier_detail'),
    path('soldier/<int:pk>/update/', views.SoldierUpdateView.as_view(), name='soldier_update'),
    path('soldier/<int:pk>/delete/', views.SoldierDeleteView.as_view(), name='soldier-delete'),
    path('', RedirectView.as_view(url='/fake_gundori/soldier/', permanent=True)),
]
