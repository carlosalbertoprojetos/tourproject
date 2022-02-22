from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

from .forms import RegisterClientForm
from .models import Client 

def list_view(request):
	list_client = Client.objects.all()	
	return render(request, "client_list.html", {"client":list_client})

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = RegisterClientForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "client_edit.html", context)

# update view for details
def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(Client, id = id)
 
    # pass the object as instance in form
    form = RegisterClientForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "client_table.html", context)


#class RegisterClientView(CreateView):
#	model = Client
#	form_class = RegisterClientForm
#	template_name = 'client/client_register.html'

#class UpdateClienteView(UpdateView):
#    model = Client
#    form_class = RegisterClientForm
#    template_name = 'client/client_edit.html'