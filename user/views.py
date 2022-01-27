from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import EditUserForm, SignupComplementForm
from .models import User


@login_required
def edit_user_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = EditUserForm(instance=user)

    if(request.method == 'POST'):
        form = EditUserForm(request.POST, instance=user)

        if(form.is_valid()):
            user = form.save(commit=False)
            user.document_kind = form.cleaned_data['document_kind']
            user.document_number = form.cleaned_data['document_number']
            user.document_image = form.cleaned_data['document_image']
            user.postal_code = form.cleaned_data['postal_code']
            user.street = form.cleaned_data['street']
            user.number = form.cleaned_data['number']
            user.complement = form.cleaned_data['complement']
            user.city = form.cleaned_data['city']
            user.state = form.cleaned_data['state']

            user.save()

            return redirect('user:edit_user', user.pk)
        else:
            return render(request, 'user/edit_user.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'user/edit_user.html', {'form': form})




@user_passes_test(lambda u: u.is_superuser)
def list_users(request):
    '''
    Lista usuários cadastrados
    '''
    object = User.objects.filter(is_superuser=False)
    context = {
        'object': object,
    }
    return render(request, 'user/list_users.html', context)


@user_passes_test(lambda u: u.is_superuser)
def edit_user_admin(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = EditUserForm(instance=user)

    if(request.method == 'POST'):
        form = EditUserForm(request.POST, instance=user)

        if(form.is_valid()):
            user = form.save(commit=False)
            user.document_kind = form.cleaned_data['document_kind']
            user.document_number = form.cleaned_data['document_number']
            user.document_image = form.cleaned_data['document_image']
            user.postal_code = form.cleaned_data['postal_code']
            user.street = form.cleaned_data['street']
            user.number = form.cleaned_data['number']
            user.complement = form.cleaned_data['complement']
            user.city = form.cleaned_data['city']
            user.state = form.cleaned_data['state']

            user.save()

            return redirect('user:list_users')
        else:
            return render(request, 'user/edit_user.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'user/edit_user.html', {'form': form})


class SignupComplementView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'account/signup_2.html'
    form_class = SignupComplementForm
    success_url = reverse_lazy('user:dashboard')

    def get_object(self):
        self.object = self.request.user
        return self.object

    def get_initial(self):
        initials = {}
        for field in self.form_class._meta.fields:
            initials[field] = getattr(self.object, field, '')
        return initials

    def form_valid(self, form):

        form.save()
        # logout(self.request)
        return HttpResponseRedirect(self.get_success_url())


signup_step_2 = SignupComplementView.as_view()
