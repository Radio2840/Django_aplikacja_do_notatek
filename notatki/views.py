from django.shortcuts import render, redirect
from .form import NoteForm
from .models import Note




def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form} )