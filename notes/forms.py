from django import forms
from .models import Note

# Ye form create aur update ke liye use hoga
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']