from django import forms
from .models import MPeople
from django_localflavor_br.forms import BRCPFField, BRPhoneNumberField


class RegisterForm(forms.ModelForm):

	cpf = BRCPFField(widget=forms.TextInput(attrs={'placeholder': 'Only numbers'}))
	phone = BRPhoneNumberField(widget=forms.TextInput(attrs={'placeholder': 'Only numbers'}))	

	class Meta:
		model = MPeople

		widgets = {
			'cep': forms.TextInput(attrs={'placeholder': 'XXXXX-XXX or only numbers'}),
			'gender': forms.TextInput(attrs={'placeholder': 'M for Male and F for Female'}),
			'birthday': forms.DateInput(attrs={'placeholder': 'DD/MM/YYYY', 'format': '%d/%m/%Y'}),
		}
		
		birthday = forms.DateField()

		fields = ('name', 'address', 'city', 'state', 'country', 'cep', 'phone', 'gender', 'email', 'birthday', 'cpf')


class SearchForm(forms.ModelForm):

	phone = BRPhoneNumberField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Only numbers'}))
	name = forms.CharField(required=False)


	class Meta:
		model = MPeople

		fields = ('name', 'phone')


class FilterForm(forms.ModelForm):
	'''Filtrate with optional parameters: age, gender or city'''

	age = forms.ModelChoiceField(widget=forms.Select(), queryset=MPeople.objects.values('birthday'))

	class Meta:
		model = MPeople

		fields = ('age',)