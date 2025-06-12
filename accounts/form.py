from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm ,SetPasswordForm

#



error_messages= {
    'required':'this field is required',
    'max_length': 'The entered length exceeds the allowed limit',
}

class Login_Form(forms.Form):
    username = forms.CharField(max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': ' Enter Username'}),
                        error_messages=error_messages)

    password = forms.CharField(max_length=20,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-lg',
                    'placeholder': ' Enter Password',
                    'autocomplete': 'off'}),
                        error_messages=error_messages)


#sing up
class Register_Form(forms.Form):
    username = forms.CharField(max_length=20,widget=forms.TextInput
        (attrs={'class': 'form-control',
                'placeholder': ' Enter Username'}),
                 error_messages=error_messages)

    password = forms.CharField(max_length=20,widget=forms.PasswordInput
        (attrs={'class': 'form-control',
                'placeholder': ' Enter Password'}),
                    error_messages=error_messages)

    email = forms.EmailField(widget=forms.TextInput
        (attrs={'class': 'form-control',
                'placeholder': ' Enter Email'}))



    def clean_username(self):
        username_input = self.cleaned_data.get('username')
        user=User.objects.filter(username=username_input)
        if user:
            raise ValidationError('this name has already been taken')
        return username_input


    def clean_email(self):
        email_input = self.cleaned_data.get('email')
        user=User.objects.filter(email=email_input)
        if user:
            raise ValidationError('this email has already been taken')
        return email_input


class EditProfileForm(forms.Form):

    about_me=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    avatar = forms.ImageField(widget=forms.FileInput, required=False,help_text='optional')


    email = forms.EmailField(widget=forms.TextInput
        (attrs={'class': 'form-control', 'placeholder': ' Enter your email'}))

    username = forms.CharField(max_length=20,widget=forms.TextInput
        (attrs={'class': 'form-control', 'placeholder': ' Enter your username'}))

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user=user

    def clean_username(self):
        username_input = self.cleaned_data.get('username')
        if self.user and self.user.username == username_input:
            return username_input
        user=User.objects.filter(username=username_input).exists()
        if user:
            raise ValidationError('this name has already been taken')
        return username_input


    def clean_email(self):
        email_input = self.cleaned_data.get('email')
        if self.user and self.user.email == email_input:
            return email_input
        user=User.objects.filter(email=email_input).exists()
        if user:
            raise ValidationError('this email has already been taken')
        return email_input



class ChangepasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'form-control', 'placeholder': '  password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'form-control', 'placeholder': '  New password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'form-control', 'placeholder': '  New password'}))
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


def password_reset():
    pass

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=70,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email',
            'id': 'typeEmailX',
        }),
    )

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New Password",
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter new password',
            'id': 'new_password1',
        }),
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        max_length=50,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm new password',
            'id': 'new_password2',
        }),
    )