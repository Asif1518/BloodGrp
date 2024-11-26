from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_donor, name='register_donor'),
    path('update/<int:donor_id>/', views.update_donation, name='update_donation'),
    path('', views.donor_list, name='donor_list'),
]
