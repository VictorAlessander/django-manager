from django.shortcuts import render, redirect
from .forms import RegisterForm, SearchForm, FilterForm
from .models import MPeople
from django.shortcuts import get_object_or_404
import re

# Create your views here.

class People(object):

	def index(request):
		return render(request, 'index.html')


	def register(request):
		if request.method == 'POST':
			form = RegisterForm(request.POST)

			if form.is_valid():
				user = form.save()
				user.save()
				return redirect('/register/')

		else:
			form = RegisterForm()

		return render(request, 'register.html', {'register_form': form})


	def list_registers(request):
		registers = MPeople.objects.all()
		
		if request.method == 'POST':
			form = FilterForm(request.POST or None)

			if form.is_valid():

				context = {
					'age': request.POST['age'],
					'gender': request.POST['gender'],
					'city': request.POST['city'],
				}

				if context['age']:
					age_choosed = re.sub("[''{ birthday: datetime.date()}]", '', context['age'])
					age_choosed = re.sub('[,]', '-', age_choosed)

					registers = MPeople.objects.filter(birthday=age_choosed)

				elif context['city']:
					registers = MPeople.objects.filter(city=form.cleaned_data.get('city'))

				elif request.POST['gender']:
					registers = MPeople.objects.filter(gender=form.cleaned_data.get('gender'))

		else:
			form = FilterForm()

		return render(request, 'list.html', {'registers': registers, 'form_filter': form})


	def edit_register(request, id):
		user_id = MPeople.objects.filter(id=id)

		form_user = get_object_or_404(MPeople, id=user_id)
		
		if request.method == 'POST':
			form = RegisterForm(request.POST, instance=form_user)

			if form.is_valid():
				user = form.save()
				user.save()
				return redirect('/list_registers/')

		else:
			form = RegisterForm(instance=form_user)

		return render(request, 'edit_register.html', {'form_edit_register': form})


	def remove_register(request, id):
		user_id = get_object_or_404(MPeople, id=id)
		user_id.delete()

		return redirect('/list_registers/')

	def search_register(request):

		search = None

		if request.method == 'GET':
			form_search = SearchForm(request.GET)

			if form_search.is_valid():

				field_content = {
					'name': form_search.cleaned_data.get('name'),
					'phone': form_search.cleaned_data.get('phone'),
					}

				if field_content['name'] != "" and field_content['phone'] != "":
					search = MPeople.objects.filter(name=field_content['name'], phone=field_content['phone'])

				elif field_content['name'] != "":
					search = MPeople.objects.filter(name=field_content['name'])

				elif field_content['phone'] != "":
					search = MPeople.objects.filter(phone=field_content['phone'])


		else:
			form_search = SearchForm()

		return render(request, 'search_register.html', {'form': form_search, 'search': search})