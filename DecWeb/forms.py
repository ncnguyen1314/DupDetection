from django import forms
from .models import Pair

class PostForm(forms.ModelForm):
    class Meta:
        model = Pair
        fields =  ('firstSentence', 'secondSentence',)
        print(fields)