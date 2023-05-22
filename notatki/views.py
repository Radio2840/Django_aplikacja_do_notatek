from django.shortcuts import render, redirect, get_object_or_404
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

def note_detail(request, year, month, day):
    note = get_object_or_404(Note, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'note': note})