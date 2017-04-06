from django import forms
from .models import MPeople
from django_localflavor_br.forms import BRCPFField, BRPhoneNumberField


class RegisterForm(forms.ModelForm):

	cpf = BRCPFField()

	class Meta:
		model = MPeople

		widgets = {
			'phone': forms.TextInput(attrs={'placeholder': 'Just numbers'}),
			'gender': forms.TextInput(attrs={'placeholder': 'M for Male and F for Female'}),
			'birthday': forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY'}),
			'cpf': forms.TextInput(attrs={'placeholder': 'XXX.XXX.XXX-XX or 11 digits'})
		}

		phone = BRPhoneNumberField()
		
		birthday = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'))

		fields = ('name', 'address', 'phone', 'gender', 'email', 'birthday', 'cpf')
