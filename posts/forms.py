from django import forms
from .models import Posts


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['content', 'image', 'category']


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['content', 'image', 'category']

    def save(self, commit=True):
        post = self.instance
        post.content = self.cleaned_data['content']
        post.category = self.cleaned_data['category']

        if self.cleaned_data['image']:
            post.image = self.cleaned_data['image']
        if commit:
            post.save()
        return post


