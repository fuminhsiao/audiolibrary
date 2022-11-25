from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from membership.models import UserDetail


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ('speakers',)