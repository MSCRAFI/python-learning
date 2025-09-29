from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data['title']
        if Post.objects.filter(title=title).exists():
            raise forms.ValidationError("Title already exists")
        return title