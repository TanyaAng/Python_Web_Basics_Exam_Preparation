from django import forms

from Notes.app.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Note.objects.all().delete()
            return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')


class DeleteNoteForm(forms.ModelForm):
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
        model = Note
        fields = ('title', 'content', 'image_url')
