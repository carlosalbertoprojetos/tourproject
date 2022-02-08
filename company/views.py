from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from user.models import User

from .forms import EditCompanyForm, Signup2Form
from .models import Company


class Signup2View(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'company/company_signup.html'
    form_class = Signup2Form
    success_url = reverse_lazy('user:dashboard')

    def get_object(self):
        self.object = self.request.user
        return self.object

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user_id = self.request.user.id
        obj.save()
        return super().form_valid(form)


signup_step_2 = Signup2View.as_view()


@user_passes_test(lambda u: u.is_superuser)
def companies_list(request):
    object = Company.objects.all()
    context = {
        'object': object,
    }

    return render(request, 'user/table.html', context)


@login_required
def company_edit(request, pk):

    notregister = Company.objects.filter(user_id=pk)
    if not notregister:
        return redirect('company:signup2')

    user = get_object_or_404(Company, user_id=pk)
    form = EditCompanyForm(instance=user)

    if request.method == 'POST':
        form = EditCompanyForm(request.POST,
                               request.FILES, instance=user)

        if form.is_valid():
            user = form.save(commit=True)
            return redirect('company:company_edit', user.pk)
        else:
            return render(request, 'company/company_edit.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'company/company_edit.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def company_edit_admin_view(request, pk):
    user = get_object_or_404(Company, pk=pk)
    form = EditCompanyForm(instance=user)

    if request.method == 'POST':
        form = EditCompanyForm(request.POST or None,
                               request.FILES, instance=user)

        if form.is_valid():
            user = form.save(commit=True)
            return redirect('user:company_edit', user.pk)
        else:
            return render(request, 'company/company_edit.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'company/company_edit.html', {'form': form})
