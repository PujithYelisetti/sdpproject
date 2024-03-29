from django import forms
from .models import *

class ReviewForm(forms.ModelForm):
    class Meta:
        model = TouristReview
        fields = ['text', 'rating', 'image']