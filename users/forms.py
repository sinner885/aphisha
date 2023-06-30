from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Div
from crispy_forms.bootstrap import Field

from allauth.account.forms import LoginForm as AllauthLoginForm
from allauth.account.forms import SignupForm as AllauthSignupForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class LoginForm(AllauthLoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.field_class = 'login-form-style-3'
        #self.helper.add_input(Submit('submit', 'Войти',css_class="fa fa-angle-right"))
        
        # Изменение класса стилей полей
        self.helper.layout = Layout(
            Div(
                Field('login', placeholder='Введіть E-mail адресу'),
                Field('password', placeholder='Введіть пароль', autocomplete='off'),
            ),
            Submit('submit', 'Увійти'),
        )


class SignupForm(AllauthSignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        #self.helper.add_input(Submit('submit', 'Войти',css_class="fa fa-angle-right"))
        self.helper.field_class = 'login-form-style-3'
        
        # Изменение класса стилей полей
        self.helper.layout = Layout(
            Div(
                Field('email', placeholder='E-mail адресa'),
                Field('password1', placeholder='пароль'),
            ),
            Submit('submit', 'Вперед'),
        )