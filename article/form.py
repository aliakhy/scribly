from django import forms
from categories.models import Category
from article.models import Article

error_messages= {
    'required':'this field is required',
}
class Articlecreate(forms.Form):
    title = forms.CharField( max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder': ' title'}),error_messages=error_messages)
    text = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'txt'}),error_messages=error_messages)
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}),error_messages=error_messages)
    is_show = forms.BooleanField(required=False)

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control select2'
        }),
        error_messages={
            'required': 'Select at least one category.',
            'invalid_choice': 'Invalid category.'
        }
    )





class Articleedite(forms.Form):
    title = forms.CharField( max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}),error_messages=error_messages)
    text = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'class':'form-control'}),error_messages=error_messages)
    picture = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}),error_messages=error_messages,required=False)
    is_show = forms.BooleanField(required=False)
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control select2'
        }),
        error_messages={
            'required': 'Select at least one category.',
            'invalid_choice': 'Invalid category.'
        }
    )