from django import forms
from django.core.exceptions import ValidationError
from .models import User


# class RegistrationForm(forms.Form):
#     attrs = {'class': "form-control",}
#     email = forms.EmailField(widget=forms.EmailInput(attrs=attrs))
#     user_name = forms.CharField(widget=forms.TextInput(attrs=attrs))
#     first_name = forms.CharField(widget=forms.TextInput(attrs=attrs))
#     last_name = forms.CharField(widget=forms.TextInput(attrs=attrs), required=False)
#     password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs=attrs))
#     password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs=attrs))
#
#     class Meta:
#         model = User
#         fields = ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2')
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError(
#                 self.error_messages['password_mismatch'],
#                 code='password_mismatch',
#             )
#         return password2


class RegistrationForm(forms.ModelForm):
    attrs = {'class': "form-control", }
    last_name = forms.CharField(widget=forms.TextInput(attrs=attrs), required=False)
    password1 = forms.CharField(min_length=8, label="Password", widget=forms.PasswordInput(attrs=attrs))
    password2 = forms.CharField(min_length=8, label="Password confirmation", widget=forms.PasswordInput(attrs=attrs))

    class Meta:
        attrs = {'class': "form-control", }
        model = User
        fields = ('email', 'user_name', 'first_name', 'last_name', 'password1', 'password2')
        labels = {
            'user_name': 'Username',
        }
        widgets = {
            'email': forms.EmailInput(attrs=attrs),
            'user_name': forms.TextInput(attrs=attrs),
            'first_name': forms.TextInput(attrs=attrs),
            'password1': forms.PasswordInput(attrs=attrs),
            'password2': forms.PasswordInput(attrs=attrs),
        }

    def clean(self):
        super(RegistrationForm, self).clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 == password2:
            self.add_error('password2', 'Password must match')

    def save(self, commit=True):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('user_name')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        password = self.cleaned_data.get('password1')
        return User.objects.create_user(email, username, first_name, last_name, password)


