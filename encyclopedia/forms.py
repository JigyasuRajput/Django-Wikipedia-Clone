from django import forms

class NewPageForm(forms.Form):
    title = forms.CharField(label='Create a New Page', max_length=100)
    content = forms.CharField(widget=forms.Textarea, label='Content')