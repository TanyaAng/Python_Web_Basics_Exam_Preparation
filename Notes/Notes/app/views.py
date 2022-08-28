from django.shortcuts import render, redirect

from Notes.app.forms import CreateProfileForm, DeleteProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from Notes.app.models import Profile, Note


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    notes = Note.objects.all()
    if not profile:
        return redirect('profile create')
    context = {
        'profile': profile,
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def create_note(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateNoteForm()
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    profile = get_profile()
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        assert isinstance(form.is_valid, object)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'form': form,
        'profile': profile,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    profile = get_profile()
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteNoteForm(instance=note)
    context = {
        'form': form,
        'profile': profile,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    profile = get_profile()
    note = Note.objects.get(pk=pk)
    context = {
        'profile': profile,
        'note': note,
    }
    return render(request, 'note-details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()
    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    total_notes = len(notes)
    context = {
        'profile': profile,
        'notes': notes,
        'total_notes': total_notes
    }
    return render(request, 'profile.html', context)


def delete_profile(request):
    profile = get_profile()
    form = DeleteProfileForm(request.POST, instance=profile)
    form.save()
    return redirect('home page')
