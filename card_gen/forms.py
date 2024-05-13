from django import forms

from . models import Config, Contact

class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config
        exclude = ["qr_code_image", "slug", "vcard_address"]
        labels = {
            "name": "Twoje imię i nazwisko",
            "company": "Nazwa firmy",
            "phone_number": "Numer telefonu",
            "email_address": "Adres email",
            "photo": "Zdjęcie (najlepiej kwadrat)",
            "vcard_address": "Adres vcard",
        }


class ContactPhoneForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["phone_number"]
        labels = {"phone_number" : "Wpisz swój numer telefonu...",}


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ["phone_number", "date", "topic"]
        labels = {
            "name": "Twoje imię i nazwisko",
            "email_address": "Adres email",
            "company": "Firma / miejsce kontaktu",
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["date", "topic"]
        labels = {
            "date": "Data",
            "topic": "Temat",
        }
