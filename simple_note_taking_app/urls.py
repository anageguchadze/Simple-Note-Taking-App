from django.contrib import admin
from django.urls import path
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add_note, name='add_note'),
    path('edit/<str:title>/', views.edit_note, name='edit_note'),
    path('delete/<str:title>/', views.delete_note, name='delete_note'),
]
