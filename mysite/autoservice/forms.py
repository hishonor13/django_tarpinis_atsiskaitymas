from django import forms
from .models import Comment
# from tinymce.models import HTMLField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'for_order', 'text',)
        
        widgets = {
            # 'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'for_order': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }