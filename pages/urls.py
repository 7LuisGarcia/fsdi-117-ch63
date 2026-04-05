from django.urls import path
from pages import views

urlpatterns = [
    path('about_me/', views.about_me_view, name='about_me'),
    path('experience/', views.experience_view, name='experience'),
    path('projects/', views.projects_view, name='projects'),
    path('contact', views.contact_view, name='contact'),
]