from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import login_required

# Sare notes show karega
@login_required
def note_list(request):
    notes = Note.objects.filter(author=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})

# Note create karna
@login_required
def create_note(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit=False)
        note.author = request.user
        note.save()
        return redirect('note_list')
    return render(request, 'notes/create_note.html', {'form': form})

# Note update karna
@login_required
def update_note(request, id):
    note = get_object_or_404(Note, id=id, author=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'notes/create_note.html', {'form': form})

# Note delete karna
@login_required
def delete_note(request, id):
    note = get_object_or_404(Note, id=id, author=request.user)
    note.delete()
    return redirect('note_list')
