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

	def __init__(self, *args, **kwargs):
		super(FilterForm, self).__init__(*args, **kwargs)

		database = MPeople.objects.all()

		age_choices = database.values('birthday').distinct()
		iage_choices = [('', 'None')] + [(id, id) for id in age_choices]
		self.fields['birthday'] = forms.ChoiceField(choices=iage_choices, widget=forms.Select(), required=False, localize=True)

		gender_choices = database.values_list('gender', flat=True).distinct()
		igender_choices = [('', 'None')] + [(id, id) for id in gender_choices]
		self.fields['gender'] = forms.ChoiceField(choices=igender_choices, widget=forms.Select(), required=False)

		city_choices = database.values_list('city', flat=True).distinct()
		icity_choices = [('', 'None')] + [(id, id) for id in city_choices]
		self.fields['city'] = forms.ChoiceField(choices=icity_choices, widget=forms.Select(), required=False)

	class Meta:
		model = MPeople

		fields = ('birthday', 'gender', 'city')