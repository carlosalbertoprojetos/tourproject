from django.shortcuts import render
from django.contrib import messages


from .models import Curso


def Lista_Cliente(request):
	lista_clientes = Curso.objects.all()
	#messages.success(request, "Cursos Listados")
	return render(request, "client_table.html", {"clientes":lista_clientes})