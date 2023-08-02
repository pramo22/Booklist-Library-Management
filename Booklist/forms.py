from django import forms
from .models import BookTask

class BookForm(forms.ModelForm):
    class Meta:
        model = BookTask
        fields = ['cover','title','price','author','description','book','complete']