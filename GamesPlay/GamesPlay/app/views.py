from django.shortcuts import render, redirect

from GamesPlay.app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, CreateGameForm, EditGameForm, \
    DeleteGameForm
from GamesPlay.app.models import Profile, Game


def get_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]
    return None


def home_page(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)


def dashboard(request):
    profile = get_profile()
    games = Game.objects.all()
    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGameForm()
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'create-game.html', context)


def details_game(request, pk):
    profile=get_profile()
    game = Game.objects.get(pk=pk)
    context = {
        'game': game,
        'profile':profile,
    }
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    profile = get_profile()
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)
    context = {
        'profile': profile,
        'form': form,
        'game': game,

    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)
    context = {
        'profile': profile,
        'form': form,
        'game': game,

    }
    return render(request, 'delete-game.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'create-profile.html', context)


def details_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    total_games = len(games)
    if games:
        average_rating = sum([game.rating for game in games]) / total_games
    else:
        average_rating = 0
    context = {
        'profile': profile,
        'games': games,
        'total_games': total_games,
        'average_rating': average_rating
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)
