from django import forms
from django.forms import ModelForm
from django.template import Template
from django.contrib.auth.forms import User
from django.contrib.auth.forms import AuthenticationForm
from fieldbook import forms as fieldbook_forms
from material import Layout, Row, Column, Fieldset, Span2, Span3, Span5, Span6, Span10
from . import form_mixin as forms


class MaterialLoginForm(AuthenticationForm):
    template = Template("""
    {% form %}
        {% part form.username prefix %}<i class="material-icons prefix">account_box</i>{% endpart %}
        {% part form.password prefix %}<i class="material-icons prefix">lock</i>{% endpart %}
    {% endform %}
    """)

    buttons = Template("""
        <a href="{% url 'registration' %}" class="waves-effect waves-teal btn-flat">Register</a>
        <button class="waves-effect waves-light btn" type="submit">Login</button>
    """)

    title = "Fieldbook Login form"


class MaterialRegistrationForm(fieldbook_forms.RegistrationForm):
    layout = Layout('fieldbook_book','username',
                    Row('password', 'password_confirm'),
                    Fieldset('Pesonal details',
                             Row('first_name', 'last_name'), 'email')
                    )

    template = Template("""
    {% form %}
        {% part form.fieldbook_book prefix %}<i class="material-icons prefix">book</i>{% endpart %}
        {% part form.username prefix %}<i class="material-icons prefix">account_box</i>{% endpart %}
        {% part form.email prefix %}<i class="material-icons prefix">email</i>{% endpart %}
        {% part form.password prefix %}<i class="material-icons prefix">lock_open</i>{% endpart %}
    {% endform %}
    """)

    buttons = Template("""
        <button class="waves-effect waves-light btn" type="submit">Submit</button>
    """)

    title = "Fieldbook Registration form"
