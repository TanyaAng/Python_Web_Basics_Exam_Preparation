from django import forms
from django.forms import PasswordInput

from GamesPlay.app.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': PasswordInput(
                attrs={'placeholder': '********', 'autocomplete': 'off', 'data-toggle': 'password'}),

        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password', 'first_name', 'last_name', 'profile_picture')
        widgets={
            'password': PasswordInput(attrs={'placeholder':'********','autocomplete': 'off','data-toggle': 'password'}),

        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Game.objects.all().delete()
            return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance

    class Meta:
        model = Game
        fields = '__all__'
