from django.contrib.auth.models import User
from django.utils.text import slugify
from django.views.generic.edit import DeleteView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView


from .form import NoteForm
from .models import Note


# def note_list(request):
#    notes = Note.objects.all()
#    return render(request, 'notes/note_list.html', {'notes': notes})


def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = User.objects.get(id=1)
            if not note.slug:  # Sprawdź, czy slug jest pusty
                note.slug = slugify(note.title)  # Wygeneruj slug na podstawie tytułu
            note.save()
            return redirect('notatki:note_detail', year=note.created.year, month=note.created.strftime('%m'),
                            day=note.created.strftime('%d'), note=note.slug)
    else:
        form = NoteForm()
    return render(request, 'create_note.html', {'form': form})


def note_detail(request, year, month, day, note):
    note = get_object_or_404(Note, slug=note,
                             created__year=year,
                             created__month=month,
                             created__day=day)
    return render(request, 'detail.html', {'note': note})


# class NoteDetailView(DetailView):
#    model = Note
#    context_object_name = 'note'
#   template_name = 'detail.html'


def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect(reverse('notes:index'))
            return redirect('notatki:note_detail', year=note.created.year, month=note.created.strftime('%m'),
                            day=note.created.strftime('%d'), note=note.slug)
    else:
        form = NoteForm(instance=note)

    context = {'form': form}
    return render(request, 'edit_note.html', context)


class NotesListView(ListView):
    queryset = Note.objects.all()
    context_object_name = 'note'
    paginate_by = 4
    template_name = 'lista_notatek.html'


class UsunNotatke(DeleteView):
    model = Note
    success_url = reverse_lazy('notatki:notes_list')
    template_name_suffix = '_usun'