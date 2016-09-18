from django import forms


class ViewComment(forms.Form):
    comment_id = forms.CharField()
