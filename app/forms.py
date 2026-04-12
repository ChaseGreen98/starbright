from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.forms import ModelForm
from app.models import *

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )


class CustomAuthenticationForm(AuthenticationForm):
    pass


class CustomPasswordChangeForm(PasswordChangeForm):
    pass


class UserUpdateForm(ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
        )


class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu_Item
        fields = (
            'name',
            'category',
            'description',
            'price',
            'is_featured',
            'image',
        )

    image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

class NewsForm(ModelForm):

    class Meta:
        model = Newsletter
        fields = (
            'title', 
            'para_one',
            'para_two',
            'para_three',
        )

class MerchForm(ModelForm):

    class Meta:
        model = Merch_Item
        fields = (
            'name', 
            'description',
            'price',
            'is_featured',
            'image',
        )

    image = forms.ImageField(required=False)
