from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from user.models import User

from django.forms import inlineformset_factory

from .forms import CompanyForm, PhoneForm
from .models import Company, Phone, SocialMedia


# class Signup2View(LoginRequiredMixin, CreateView):
#     model = Company
#     form_class = Signup2Form
#     template_name = 'company/company_signup.html'
#     success_url = reverse_lazy('user:dashboard')

#     def post(self, request, *args, **kwargs):
#         form = Signup2Form(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             company = form.save(commit=True)
#             company.save()
#             user = request.user
#             user.company_id = company.id
#             user.is_staff = True
#             user.save()
#             messages.success(request, 'Empresa cadastrada com sucesso!!!')
#             return self.form_valid(form)
#         else:
#             return super(Signup2View, self).post(request, *args,
#                                                  **kwargs)


# signup_step_2 = Signup2View.as_view()


def signup_step_2(request):

    if request.method == 'POST':
        form = CompanyForm(request.POST)
        
        Formset_phone_Factory = inlineformset_factory(Company, Phone, form=PhoneForm, extra=1, can_delete=False)
        phone_form = Formset_phone_Factory(request.POST)
        
        Formset_social_Factory = inlineformset_factory(Company, SocialMedia, fields=('socmedia',), extra=1, can_delete=False)        
        socmedia_form = Formset_social_Factory(request.POST)

        if form.is_valid() and phone_form.is_valid() and socmedia_form.is_valid():
            company = form.save()
            user = request.user
            user.company_id = company.id
            user.is_staff = True
            user.save()
            phone_form.instance = company
            phone_form.save()
            socmedia_form.instance = company
            socmedia_form.save()
            messages.success(request, 'Empresa cadastrada com sucesso!!!')
            return redirect('user:dashboard')
            
        else:
            context = {
                'form': form,
                'formset_phone': phone_form,
                'formset_socmedia': socmedia_form
            }
        return render(request, 'dashboard.html', context)


    elif request.method == 'GET':
        company = CompanyForm()
        
        Formset_Factory = inlineformset_factory(Company, Phone, PhoneForm, extra=1, can_delete=False)
        phone = Formset_Factory()
                        
        Formset_social_Factory = inlineformset_factory(Company, SocialMedia, fields=('socmedia',), extra=3, can_delete=False)        
        socmedia = Formset_social_Factory()
        
        context = {
            'form': company,
            'formset_phone': phone,
            'formset_socmedia': socmedia
            }
        return render(request, 'company/company_signup.html', context)


@user_passes_test(lambda u: u.is_superuser)
def companies_list(request):
    object = Company.objects.all()
    context = {
        'object': object,
    }

    return render(request, 'company/companies_list.html', context)


@user_passes_test(lambda u: u.option != '2')
def company_update(request, pk):

    user = request.user
    try:
        if user.is_superuser:
            company = get_object_or_404(Company, pk=pk)
        else:
            company = get_object_or_404(Company, pk=user.company_id)

        form = CompanyForm(instance=company)
        if request.method == 'POST':
            form = CompanyForm(
                request.POST or None, request.FILES or None, instance=company)

            if form.is_valid():
                company = form.save(commit=True)
                messages.success(request, 'Dados alterados com sucesso!!!')
                if user.is_superuser:
                    return redirect('company:companies_list')
                else:
                    return redirect('company:company_update', user.company_id)

            else:
                return render(request, 'company/company_update.html', {'form': form})

        elif request.method == 'GET':
            return render(request, 'company/company_update.html', {'form': form})

    except:
        return redirect('company:signup2')


@user_passes_test(lambda u: u.is_staff)
def company_agents_list(request):
    user = request.user
    form = User.objects.filter(company_id=user.company_id)
    template_name = 'company/company_users_list.html'

    context = {
        'form': form
    }
    return render(request, template_name, context)
