from django.forms import ModelForm, PasswordInput 
from password_manager.models import Login, Card, PIN, SecureNote


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ["name", "username", "password", "website", "note"]


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ["name", "cardholder", "number", "expiration_date", "cvv"]


class PINForm(ModelForm):
    class Meta:
        model = PIN
        fields = ["name", "code", "note"]


class SecureNoteForm(ModelForm):
   class Meta:
       model = SecureNote 
       fields = ["name", "notes"]

