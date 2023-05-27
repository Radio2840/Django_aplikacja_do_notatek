from django.urls import path, include
from rest_framework import routers

from notatki import views

app_name = 'notatki'

urlpatterns = [
    path('', views.NotesListView.as_view(), name='notes_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:note>', views.note_detail, name='note_detail')
]