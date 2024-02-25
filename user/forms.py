from django import forms


class RegisterForm(forms.Form):
    avatar = forms.ImageField(required=False, label='Фото профиля')
    first_name = forms.CharField(max_length=100, required=False, label='Имя')
    last_name = forms.CharField(max_length=100, required=False, label='Фамилия')
    bio = forms.CharField(max_length=500, required=False, label='Биография', widget=forms.Textarea)
    username = forms.CharField(max_length=100, required=True, label='Имя пользователя')
    email = forms.EmailField(required=True, label='Адрес электронной почта')
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput, label='Повторите')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password!= password2:
            raise forms.ValidationError("Пароли не совпадают")
        
        return cleaned_data
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label='Имя пользователя')
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput, label='Пароль')

    # def clean(self):
    #     cleaned_data = super().clean()
    #     return cleaned_data


class VerifyForm(forms.Form):
    code = forms.CharField(max_length=10, required=True)