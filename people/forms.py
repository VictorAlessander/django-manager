from django import forms
from .models import MPeople
from localflavor.br.forms import BRCPFField, BRPhoneNumberField


class RegisterForm(forms.ModelForm):

	class Meta:
		model = MPeople

		phone = BRPhoneNumberField(required=True)
		cpf = BRCPFField(required=True)
		birthday = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'))

		fields = ('name', 'address', 'phone', 'sex', 'email', 'birthday', 'cpf')