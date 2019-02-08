from django import forms
from django.contrib.auth.models import User
from rango.models import Category, Page, UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    #Inline class that does some gubbins

    class Meta:
        #Provides association between modelform and model
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")

    url = forms.URLField(max_length=200,
                         help_text="Please enter the url of the page")

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not an empty and/or doesn't start with 'http://'
        #then prepamd 'hhtt'

        if url and not url.startswith('http;//'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data


    class Meta:
         # Provide an association between the ModelForm and a model

         model = Page
         fields = ("__all__")
         exclide = ('category', )

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')


