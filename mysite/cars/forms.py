from django import forms
from .models import Review
from django.forms import ModelForm


#class ReviewForm(forms.Form):
#    first_name = forms.CharField(label='First Name', max_length=25)
#    last_name = forms.CharField(label='Last Name', max_length=25)
#    email = forms.EmailField(label='Email', max_length=25)
#    review = forms.CharField(label='Please write your review', max_length=25, 
#                             widget=forms.Textarea(attrs = {'class':'myform', 'rows':'7', 'col':'2'}))



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        labels = {
            'first_name':'Your first name',
            'last_name':'You last name',
            'stars':'Rating'
        }