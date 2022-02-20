from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from user.models import User

from .forms import CompanyEditForm, Signup2Form
from .models import Company


class Signup2View(LoginRequiredMixin, CreateView):
    model = Company
    form_class = Signup2Form
    template_name = 'company/company_signup.html'
    success_url = reverse_lazy('user:dashboard')

    def post(self, request, *args, **kwargs):
        form = Signup2Form(request.POST or None, request.FILES or None)
        if form.is_valid():
            company = form.save(commit=True)
            company.save()
            user = request.user
            user.company_id = company.id
            user.is_staff = True
            user.save()
            messages.success(request, 'Empresa cadastrada com sucesso!!!')
            return self.form_valid(form)
        else:
            return super(Signup2View, self).post(request, *args,
                                                 **kwargs)


signup_step_2 = Signup2View.as_view()


@user_passes_test(lambda u: u.is_superuser)
def companies_list(request):
    object = Company.objects.all()
    context = {
        'object': object,
    }

    return render(request, 'company/companies_list.html', context)


@user_passes_test(lambda u: u.option != '2')
def company_edit(request, pk):

    user = request.user
    try:
        if user.is_superuser:
            company = get_object_or_404(Company, pk=pk)
        else:
            company = get_object_or_404(Company, pk=user.company_id)

        form = CompanyEditForm(instance=company)
        if request.method == 'POST':
            form = CompanyEditForm(
                request.POST or None, request.FILES or None, instance=company)

            if form.is_valid():
                company = form.save(commit=True)
                messages.success(request, 'Dados alterados com sucesso!!!')
                if user.is_superuser:
                    return redirect('company:companies_list')
                else:
                    return redirect('company:company_edit', user.company_id)

            else:
                return render(request, 'company/company_edit.html', {'form': form})

        elif request.method == 'GET':
            return render(request, 'company/company_edit.html', {'form': form})

    except:
        return redirect('company:signup2')


# def company_edit_admin(request, pk):
#     user = request.user
#     if user.is_superuser:
#         company = get_object_or_404(Company, pk=pk)
#         form = CompanyEditForm(instance=company)

#         if request.method == 'POST':
#             form = CompanyEditForm(
#                 request.POST or None, request.FILES or None, instance=company)

#             if form.is_valid():
#                 company = form.save(commit=True)
#                 if user.is_superuser:
#                     return redirect('company:companies_list')
#                 else:
#                     return redirect('company:company_edit', user.company_id)

#             else:
#                 return render(request, 'company/company_edit.html', {'form': form})

#         elif request.method == 'GET':
#             return render(request, 'company/company_edit.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def company_agents_list(request):
    user = request.user
    form = User.objects.filter(company_id=user.company_id)
    template_name = 'company/company_users_list.html'

    context = {
        'form': form
    }
    return render(request, template_name, context)
