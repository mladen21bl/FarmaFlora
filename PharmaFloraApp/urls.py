from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('base', views.base, name='base'),
    path('create/', views.create_plant, name='create_plant'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plant/<int:pk>/delete/', views.delete_plant, name='delete_plant'),
    path('delete_all/', views.delete_all_plants, name='delete_all_plants'),
    path('search_by_name/', views.search_by_name, name='search_by_name'),
    path('edit_plant/<int:pk>/', views.edit_plant, name='edit_plant'),
    path('plant/<int:pk>/molecule', views.plant_detail_molecule, name='plant_detail_molecule'),
]
