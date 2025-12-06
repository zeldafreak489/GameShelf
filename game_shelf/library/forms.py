from django import forms
from .models import Review

# Generate quarter-star choices from 0.00 to 5.00
QUARTER_STAR_CHOICES = [(x/4, f"{x/4:.2f}") for x in range(0, 21)]
# Creates: (0.00, "0.00"), (0.25, "0.25"), ..., (5.00, "5.00")

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=QUARTER_STAR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': "form-control", 'rows': 3}),
        }

    def clean_rating(self):
        return float(self.cleaned_data['rating'])
