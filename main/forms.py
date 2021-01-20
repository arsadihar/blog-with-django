from django import forms
from ckeditor import fields


class CommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", "rows": 5}))


class CreatePostForm(forms.Form):
    title = forms.CharField(label="Blog Post Title", widget=forms.TextInput(attrs={'class': "form-control"}))
    subtitle = forms.CharField(label="Subtitle", widget=forms.TextInput(attrs={'class': "form-control"}))
    img_url = forms.CharField(label="Blog Image URL", widget=forms.TextInput(attrs={'class': "form-control"}))
    body = fields.RichTextFormField(label="Blog Content", widget=fields.CKEditorWidget(attrs={'class': "form-control"}))


class ContactForm(forms.Form):
    username = forms.CharField(label="Name",
                               widget=forms.TextInput(
                                   attrs={'class': "form-control", "placeholder": "Name"}))
    email = forms.EmailField(label="Email Address",
                             widget=forms.EmailInput(
                                 attrs={'class': "form-control", "placeholder": "Email Address"}))
    phone_number = forms.CharField(label="Phone Number",
                                   widget=forms.TextInput(
                                       attrs={'class': "form-control", "placeholder": "Phone Number"}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': "form-control", "placeholder": "Message", "rows": 5}))
