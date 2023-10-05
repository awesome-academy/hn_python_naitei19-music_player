from django import forms

class reportForm(forms.Form):
    song_id = forms.IntegerField(widget=forms.HiddenInput())
    reason = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Reason for reporting...'}))