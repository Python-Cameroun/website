from django import forms
from base.models import User
from django.utils.translation import gettext as _


class SignUpForm(forms.ModelForm):
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password1']

    def clean_password1(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password1 = cleaned_data.get('password1')

        if not password1:
            raise forms.ValidationError(_('You must enter the confirmation password'))
        if password != password1:
            raise forms.ValidationError(_('Your passwords must match'))

        return password1

    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')

        try:
            m_ = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(_('Your email address already exists'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = _('Your username')
        self.fields['email'].widget.attrs['placeholder'] = _('Email Address')
        self.fields['password'].widget.attrs['placeholder'] = _('Password')
        self.fields['password1'].widget.attrs['placeholder'] = _('Retype password')

        self.fields['password'].widget.attrs['autocomplete'] = 'off'
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
