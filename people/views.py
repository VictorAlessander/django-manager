from django.shortcuts import render

# Create your views here.

class People(object):

	#self.informations = 

	def index(request):
		return render(request, 'index.html')


	def register(request):
		return render(request, 'register.html', {})


#	def buscar_cadastro(request):
#		return