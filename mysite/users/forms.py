from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm,self).__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class':'w-full px-3 py-2 border border-gray-300 rounded'
            })


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
        exclude = ['password1','password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        self.fields['image'].widget.attrs.update({
            'class': 
            'w-full text-sm text-gray-500 '
            'file:mr-4 file:py-2 file:px-4 '
            'file:rounded-lg file:border-0 '
            'file:text-sm file:font-semibold '
            'file:bg-orange-500 file:text-white '
            'hover:file:bg-orange-600'
        })