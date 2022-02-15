from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import CompanyEditForm, Signup2Form
from .models import Company


class Signup2View(LoginRequiredMixin, CreateView):
    model = Company
    form_class = Signup2Form
    template_name = 'company/company_signup.html'
    success_url = reverse_lazy('user:dashboard')

    def post(self, request, *args, **kwargs):
        form = Signup2Form(request.POST or None)
        if form.is_valid():
            company = form.save(commit=True)
            company.save()
            user = request.user
            user.company_id = company.id
            user.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


signup_step_2 = Signup2View.as_view()


@user_passes_test(lambda u: u.is_superuser)
def companies_list(request):
    object = Company.objects.all()
    context = {
        'object': object,
    }

    return render(request, 'company/companies_list.html', context)


@login_required
def company_edit(request, pk, queryset=None):
    try:
        user = request.user
        if user.is_superuser:
            company = get_object_or_404(Company, pk=pk)
        else:
            company = get_object_or_404(Company, pk=user.company_id)

        form = CompanyEditForm(instance=company)
        if request.method == 'POST':
            form = CompanyEditForm(request.POST,
                                   request.FILES, instance=company)
            if form.is_valid():
                company = form.save(commit=True)
                if user.is_superuser:
                    return redirect('company:companies_list')
                else:
                    return redirect('company:company_edit', user.company_id)
            else:
                return render(request, 'company/company_edit.html', {'form': form})

        elif request.method == 'GET':
            return render(request, 'company/company_edit.html', {'form': form})

    except:
        if queryset is None:
            return redirect('company:signup2')
