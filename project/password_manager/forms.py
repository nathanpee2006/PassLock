from django.forms import ModelForm, TextInput, URLInput, Textarea, DateInput
from password_manager.models import Login, Card, PIN, SecureNote


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ["name", "username", "password", "website", "note"]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control"
            }), 
            "username": TextInput(attrs={
                "class": "form-control"
            }),
            "password": TextInput(attrs={
                "class": "form-control"
            }),
            "website": URLInput(attrs={
                "class": "form-control"
            }),
            "note": Textarea(attrs={
                "class": "form-control"
            }) 
        }

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ["name", "cardholder", "number", "expiration_date", "cvv"]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control"
            }),
            "cardholder": TextInput(attrs={
                "class": "form-control"
            }),
            "number": TextInput(attrs={
                "class": "form-control"
            }),
            "expiration_date": DateInput(attrs={
                "class": "form-control"
            }),
            "cvv": TextInput(attrs={
                "class": "form-control"
            })
        }


class PINForm(ModelForm):
    class Meta:
        model = PIN
        fields = ["name", "code", "note"]
        widgets = {
            "name": TextInput(attrs={
                "class": "form-control"
            }), 
            "code": TextInput(attrs={
                "class": "form-control"
            }), 
            "note": Textarea(attrs={
                "class": "form-control"
            }) 
        }


class SecureNoteForm(ModelForm):
   class Meta:
       model = SecureNote 
       fields = ["name", "notes"]
       widgets = {
            "name": TextInput(attrs={
                "class": "form-control"
            }), 
            "notes": Textarea(attrs={
                "class": "form-control"
            }) 
       }


