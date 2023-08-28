from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    phone_regex = RegexValidator(
        regex=r'^\+?91?\d{10}$',
        message="Phone number must be entered in the format: '+919999999999'. 10 digits allowed."
    )

    phone_no = forms.CharField(validators=[phone_regex], max_length=13)
    # phone_no = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    bio = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_no', 'first_name','last_name','password1', 'password2','bio']
        help_texts = {
            'username': None}

class TextForm(forms.Form):
    text = forms.CharField(label='Enter your text', widget=forms.Textarea, required=True)
    