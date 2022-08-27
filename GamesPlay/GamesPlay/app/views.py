from django.shortcuts import render


def home_page(request):
    context = {}
    return render(request, 'home-page.html', context)


def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)


def create_game(request):
    context = {}
    return render(request, 'create-game.html', context)


def details_game(request,pk):
    context = {}
    return render(request, 'details-game.html', context)


def edit_game(request,pk):
    context = {}
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    context = {}
    return render(request, 'delete-game.html', context)


def create_profile(request):
    context = {}
    return render(request, 'create-profile.html', context)


def details_profile(request):
    context = {}
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    context = {}
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    context = {}
    return render(request, 'delete-profile.html', context)
