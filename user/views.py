from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import EditUserForm, EditUserAdminForm, SignupComplementForm
from .models import User


@login_required
def edit_user_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = EditUserForm(instance=user)

    if request.method == 'POST':
        form = EditUserForm(request.POST or None, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=True)

            return redirect('user:edit_user', user.pk)
        else:
            return render(request, 'user/edit_user.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'user/edit_user.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def list_users(request):
    object = User.objects.all()
    context = {
        'object': object,
    }
    return render(request, 'user/list_users.html', context)


@user_passes_test(lambda u: u.is_superuser)
def edit_user_admin(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = EditUserAdminForm(instance=user)

    if request.method == 'POST':
        form = EditUserAdminForm(request.POST or None, request.FILES, instance=user)

        if form.is_valid():
            user = form.save(commit=True)

            return redirect('user:list_users')
        else:
            return render(request, 'user/edit_user_admin.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'user/edit_user_admin.html', {'form': form})


class SignupComplementView(LoginRequiredMixin, UpdateView):

    model = User
    template_name = 'account/signup_2.html'
    form_class = SignupComplementForm
    success_url = reverse_lazy('user:dashboard')

    def get_object(self):
        self.object = self.request.user
        return self.object


signup_step_2 = SignupComplementView.as_view()
