from django.shortcuts import render, redirect

from Library.main.forms import CreateUserForm, EditUserForm, DeleteUserForm, CreateBookForm, EditBookForm, \
    DeleteBookForm
from Library.main.models import Profile, Book


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def get_books():
    books = Book.objects.all()
    if books:
        return books
    return None


def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('profile create')
    books = get_books()
    context = {
        'profile': profile,
        'books': books,
    }
    return render(request, 'home-with-profile.html', context)


def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateBookForm()
    context = {
        'form': form
    }
    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditBookForm(instance=book)
    context = {
        'form': form,
        'book':book,
    }
    return render(request, 'edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    # if request.method == 'POST':
    form = DeleteBookForm(request.POST, instance=book)
    form.save()
    return redirect('home page')


def create_profile(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateUserForm()
    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def profile_page(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')
    else:
        form = EditUserForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteUserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteUserForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)
