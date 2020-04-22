# -*- coding: utf-8 -*-
from .models import Post
from django import forms

class PostCreateForm(forms.ModelForm):
    file = forms.FileField(required=False, label='Post content from file')
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'file']
    