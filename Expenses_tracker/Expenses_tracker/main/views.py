from django.shortcuts import render, redirect

from Expenses_tracker.main.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm, EditExpenseForm, \
    CreateExpenseForm, DeleteExpenseForm
from Expenses_tracker.main.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def get_expense(pk):
    expenses = Expense.objects.all()
    searched_expense = [e for e in expenses if e.pk == pk]
    if searched_expense:
        return searched_expense[0]
    return None


def home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    expenses = Expense.objects.all()
    total_expenses_price = sum([e.price for e in expenses])
    budget_left = profile.budget - total_expenses_price
    context = {
        'expenses': expenses,
        'profile': profile,
        'total_expenses_price': total_expenses_price,
        'budget_left': budget_left,
    }
    return render(request, 'home-with-profile.html', context)


def create_expense_page(request):
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateExpenseForm()
    context = {
        'form': form
    }
    return render(request, 'expense-create.html', context)


def edit_expense_page(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditExpenseForm(instance=expense)
    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def delete_expense_page(request, pk):
    expense = get_expense(pk)
    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteExpenseForm(instance=expense)
    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-delete.html', context)


def profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    expenses_count = len(expenses)
    budget_left = profile.budget - sum(e.price for e in expenses)

    context = {
        'profile': profile,
        'expenses_count': expenses_count,
        'budget_left': budget_left,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()
    context = {'form': form,
               'no_profile': True}
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    current_profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=current_profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EditProfileForm(instance=current_profile)
    context = {'form': form, }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {'form': form, }
    return render(request, 'profile-delete.html', context)
