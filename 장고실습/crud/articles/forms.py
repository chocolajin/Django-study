from dataclasses import field
from django import forms
from .models import Article,Comment

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        exclude = ('user',)
        
class CommentForm(forms.ModelForm):
    
    class Meta:
        # 사용자가 입력하는 값 확인
        model = Comment
        exclude = ('article', 'user',)
        
        