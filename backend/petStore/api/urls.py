from django.urls import path

from . import views

urlpatterns = [
    path('pet/', views.api_pet),
    path('pet/<int:pk>/', views.api_pet_detailed_view),
    path('pet/findByStatus', views.api_find_by_status),
    #path('pet/<int:pk>/uploadImage', views.api_upload_picture)
]