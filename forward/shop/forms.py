from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class MiniForm(forms.Form):
    name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    phome_number = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder': 'Ваш телефон'}))

class MessageForm(forms.Form):
    MessageName = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Ваше имя'}))
    MessageEmail = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    MessagePhomenumber = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder': 'Ваш телефон'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Сообщение'}))

