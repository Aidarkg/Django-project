from django import forms

class RegisterForm(forms.Form):
    avatar = forms.ImageField(required=False, label='Фото профиля', widget=forms.FileInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=False, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=False, label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(max_length=500, required=False, label='Биография', widget=forms.Textarea(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, required=True, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='Адрес электронной почты', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Повторите')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают")
        
        return cleaned_data
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Пароль')


class VerifyForm(forms.Form):
    code = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProfileForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(max_length=500, required=False, label='Биография', widget=forms.Textarea(attrs={'class': 'form-control'}))
    avatar = forms.ImageField(required=False, label='Фото профиля', widget=forms.FileInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, required=False, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, required=False, label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='Адрес электронной почты', widget=forms.EmailInput(attrs={'class': 'form-control'}))

