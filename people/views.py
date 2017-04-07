from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import MPeople
from django.shortcuts import get_object_or_404

# Create your views here.

class People(object):

	#global database

	#database = MPeople.objects.all()

	def index(request):
		return render(request, 'index.html')


	def register(request):
		if request.method == 'POST':
			form = RegisterForm(request.POST)

			if form.is_valid():
				user = form.save()
				user.save()
				return redirect('/')

		else:
			form = RegisterForm()

		return render(request, 'register.html', {'register_form': form})


	def list_registers(request):
		registers = MPeople.objects.all()

		return render(request, 'list.html', {'registers': registers})


	def edit_register(request, id):
		user_id = MPeople.objects.filter(id=id)

		form_user = get_object_or_404(MPeople, id=user_id)
		
		if request.method == 'POST':
			form = RegisterForm(request.POST, instance=form_user)

			if form.is_valid():
				user = form.save()
				user.save()
				return redirect('/')

		else:
			form = RegisterForm(instance=form_user)

		return render(request, 'edit_register.html', {'form_edit_register': form})


	def remove_register(request, id):
		user_id = get_object_or_404(MPeople, id=id)
		user_id.delete()

		return redirect('/')