from django import forms
from .models import Posts, PostComments


class NewPostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Posts
        fields = ['content', 'image', 'category']


class UpdatePostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

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


class NewCommentForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = PostComments
        fields = ['content', 'image']

