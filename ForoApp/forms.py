from django import forms
from ForoApp.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','descripcion','publisher','image',]

        