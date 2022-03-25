from  django import forms
from .models import *


class ContatoForm(forms.ModelForm):
	class Meta:
		model = Contato
		exclude = ('id', 'data', 'email_sent')

class CommentForm(forms.ModelForm):
	class Meta:
		model = CommentPost
		fields = ['nome', 'comentario']

