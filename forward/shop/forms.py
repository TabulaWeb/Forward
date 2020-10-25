from django import forms
from .models import Comment


class PlaceholderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.help_text

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class MiniForm(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    phome_number = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder': 'Ваш телефон'}))
