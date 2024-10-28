from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('education/', views.education_view, name='education'),
    path('experience/', views.experience_view, name='experience'),
    path('social/', views.social_view, name='social'),
]
