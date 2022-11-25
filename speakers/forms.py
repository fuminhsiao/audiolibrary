from django import forms
from speakers.models import Speaker, Comment
from django.core.files.uploadedfile import InMemoryUploadedFile
from humanize import naturalsize
from django.core.exceptions import ValidationError
from django.core import validators


class SpeakerForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    picture = forms.FileField(required=False, label='File to Upload <=' + max_upload_limit_text)
    upload_field_name = 'picture'

    class Meta:
        model = Speaker
        fields = ['model', 'speaker_type', 'manufacturer', 'text', 'picture']

        # Validate the size of the picture

    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < " + self.max_upload_limit_text + " bytes")

        # Convert uploaded File object to a picture

    def save(self, commit=True):
        instance = super(SpeakerForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture  # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()

        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)



