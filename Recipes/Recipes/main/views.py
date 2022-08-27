from django.shortcuts import render, redirect

from Recipes.main.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from Recipes.main.models import Recipe


def get_current_recipe(pk):
    return Recipe.objects.get(pk=pk)


def home_page(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_page(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateRecipeForm()

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_page(request, pk):
    recipe = get_current_recipe(pk)
    if request.method == 'POST':
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditRecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'edit.html', context)


def delete_page(request, pk):
    recipe = get_current_recipe(pk)
    if request.method == 'POST':
        form = DeleteRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteRecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'delete.html', context)


def details_page(request, pk):
    recipe = get_current_recipe(pk)
    ingredients = recipe.ingredients.split(', ')
    context = {
        'recipe': recipe,
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)
