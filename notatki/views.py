from django.views.generic.edit import DeleteVie
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .form import NoteForm
from .models import Note




#def note_list(request):
#    notes = Note.objects.all()
#    return render(request, 'notes/note_list.html', {'notes': notes})


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


def note_detail(request, year,month,day,note):
    note = get_object_or_404(Note, slug=note,
                             created__year=year,
                             created__month=month,
                             created__day=day)
    return render(request, 'detail.html', {'note': note})

#class NoteDetailView(DetailView):
#    model = Note
#    context_object_name = 'note'
#   template_name = 'detail.html'


def edit_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notes:index'))
    else:
        form = NoteForm(instance=note)

    context = {'form': form}
    return render(request, 'notes/edit_note.html', context)

class NotesListView(ListView):
    queryset = Note.objects.all()
    context_object_name = 'note'
    paginate_by = 4
    template_name = 'lista_notatek.html'
    
    
class UsunNotatke(DeleteView):
    model = Note
    success_url = reverse_lazy('lista_notatek')
    template_name_suffix = '_usun'
