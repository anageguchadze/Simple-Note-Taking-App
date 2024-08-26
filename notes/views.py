from django.shortcuts import render, redirect
from .models import Note

# Create your views here.
def index(request):
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes':notes})

def add_note(request):
    if request.method == 'POST':
        new_note = Note(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            date_created = request.POST.get('date_created'),
        )
        new_note.save()
        return redirect('index')
    return render(request, 'add_note.html')

def edit_note(request, title):
    note = Note.objects.get(title=title)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.save()
        return redirect('index')
    return render(request, 'edit_note.html', {'note': note})

def delete_note(request, title):
    note = Note.objects.get(title=title)
    if request.method == 'POST':
        note.delete()
        return redirect('index')
    return render(request, 'delete_note.html', {'note':note})