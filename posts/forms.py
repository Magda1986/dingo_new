from django import forms
from posts.models import Post, Author

class PostForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = forms.ChoiceField(
            choices=((a.id, a.nick) for a in Author.objects.all())
        )
        tags = forms.ChoiceField(
            choices=((t.word) for t in Tags.objects.all())
        )
        if not title or content:
            raise forms.ValidationError("Proszę uzupełnić wszystkie wartości")

    class Meta:
        model = Post
        fields = "__all__"
        fields = ["title", "content", "author", "tags"]


class AuthorForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        email = cleaned_data.get('email')

        if not (nick or email):
            raise forms.ValidationError("Proszę uzupełnić wszystkie wartości")

    class Meta:
        model = Author
        fields = ["nick", "email"]