from django import forms

from Library.main.models import Profile, Book


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteUserForm(forms.ModelForm):
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
        model = Profile
        fields = '__all__'


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class DeleteBookForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            return self.instance

    class Meta:
        model = Book
        fields = ()
