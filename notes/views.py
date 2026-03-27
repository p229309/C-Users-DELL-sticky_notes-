from django.shortcuts import render
from .models import Note

# Ye view sari notes ka list show karega
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})