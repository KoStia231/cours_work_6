from django import forms

from blog.models import BlogEntry
from users.forms import CustomFormMixin


class BlogEntryForm(CustomFormMixin, forms.ModelForm):
    """Форма для создания и редактирования записей блога"""

    class Meta:
        model = BlogEntry
        fields = ('title', 'contents', 'image', 'publications')
