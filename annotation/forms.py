from django import forms
from .models import Annotation


class AnnotationForm(forms.ModelForm):
    class Meta:
        model = Annotation
        fields = ["label", "description"]


# hier wird Formular definiert um daten in Datenbank einzutragen
# Felder müssen übereinstimmen mit dem, was in models.py angelegt wird