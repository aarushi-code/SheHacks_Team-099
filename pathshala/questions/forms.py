from django import forms
from .models import questions

class QuestionsForm(forms.ModelForm):

	class Meta:
		model = questions
		fields = ('description', 'questions_img')