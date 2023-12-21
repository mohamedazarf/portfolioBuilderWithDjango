from django import forms
from .models import Portfolio

class newPortflioForm(forms.ModelForm):
    class Meta:
        model=Portfolio
        fields=['who_is_you','what_does_you_do','career_summary','A_philosophy_statement','A_short_biography','Professional_accomplishments','Awards_and_honors','Transcripts_degrees_licenses_certifications','Volunteering_community_service','References_testimonials']
   