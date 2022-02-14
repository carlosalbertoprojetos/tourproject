from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import EditCompanyForm, Signup2Form
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
        user = get_object_or_404(Company, user_id=pk)
        form = EditCompanyForm(instance=user)

        if request.method == 'POST':
            form = EditCompanyForm(request.POST,
                                   request.FILES, instance=user)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.user_id = request.user
                obj.save()
                return redirect('user:dashboard')
            else:
                return render(request, 'company/company_edit.html', {'form': form})

        elif request.method == 'GET':
            return render(request, 'company/company_edit.html', {'form': form})
    except:
        if queryset is None:
            return redirect('company:signup2')


@user_passes_test(lambda u: u.is_superuser)
def company_edit_admin(request, pk):
    user = get_object_or_404(Company, pk=pk)
    form = EditCompanyForm(instance=user)

    if request.method == 'POST':
        form = EditCompanyForm(request.POST,
                               request.FILES, instance=user)

        if form.is_valid():
            user = form.save(commit=True)

            return redirect('company:companies_list')
        else:
            return render(request, 'company/company_edit.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'company/company_edit.html', {'form': form})
