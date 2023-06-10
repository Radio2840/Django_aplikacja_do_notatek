from django.urls import path, include
from rest_framework import routers

from notatki import views
from notatki.views import UsunNotatke, NotesListView

app_name = 'notatki'

urlpatterns = [
    path('', views.NotesListView.as_view(), name='notes_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:note>', views.note_detail, name='note_detail'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('usun/<int:pk>/', views.UsunNotatke.as_view(), name='usun_notatke'),
    path('create/', views.create_note, name='create_note'),
]