from django import forms
from .models import BlogModel,AppUser,Category

class BlogForm(forms.Form):
    title = forms.CharField(label='title',max_length=20)
    description = forms.CharField(label='description',widget=forms.Textarea())


class Categoryform(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields = '__all__'

