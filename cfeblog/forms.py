from django import forms

#from pagedown.widgets import PagedownWidget

from .models import CfePost


class CfePostForm(forms.ModelForm):
    #content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = CfePost
        fields = [
            "title",
            "content",
            "image",
            "draft",
            "publish",
        ]