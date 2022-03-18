from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy as _
from django.views.generic.edit import DeleteView
from user.models import User


from .forms import CompanyForm, PhoneForm
from .models import Company, CompanyDestinies, Phone, SocialMedia


def signup_step_2(request):

    if request.method == 'POST':
        form = CompanyForm(request.POST)
        
        Formset_destiny_Factory = inlineformset_factory(Company, CompanyDestinies, fields=('destiny',), extra=1, can_delete=False)        
        destiny_form = Formset_destiny_Factory(request.POST)
        
        Formset_phone_Factory = inlineformset_factory(Company, Phone, form=PhoneForm, extra=1, can_delete=False)
        phone_form = Formset_phone_Factory(request.POST)
        
        Formset_social_Factory = inlineformset_factory(Company, SocialMedia, fields=('socmedia',), extra=1, can_delete=False)        
        socmedia_form = Formset_social_Factory(request.POST)
        

        if form.is_valid() and phone_form.is_valid() and socmedia_form.is_valid() and destiny_form.is_valid():
            company = form.save()
            user = request.user
            user.company_id = company.id
            user.is_staff = True
            user.save()
            destiny_form.instance = company
            destiny_form.save()
            phone_form.instance = company
            phone_form.save()
            socmedia_form.instance = company
            socmedia_form.save()
            messages.success(request, 'Empresa cadastrada com sucesso!!!')
            return redirect('user:dashboard')
            
        else:
            context = {
                'form': form,
                'formset_destiny' : destiny_form,
                'formset_phone': phone_form,
                'formset_socmedia': socmedia_form
            }
        return render(request, 'dashboard.html', context)


    elif request.method == 'GET':
        form = CompanyForm()
        
        Formset_destiny_Factory = inlineformset_factory(Company, CompanyDestinies, fields=('destiny',), extra=1, can_delete=False)        
        destiny_form = Formset_destiny_Factory()
        
        Formset_phone_Factory = inlineformset_factory(Company, Phone, form=PhoneForm, extra=1, can_delete=False)
        phone_form = Formset_phone_Factory()
        
        Formset_social_Factory = inlineformset_factory(Company, SocialMedia, fields=('socmedia',), extra=1, can_delete=False)        
        socmedia_form = Formset_social_Factory()
        
        context = {
            'form': form,
            'formset_destiny' : destiny_form,
            'formset_phone': phone_form,
            'formset_socmedia': socmedia_form
        }
        return render(request, 'company/company_signup.html', context)


@user_passes_test(lambda u: u.is_superuser)
def companies_list(request):
    object = Company.objects.all()
    context = {
        'object': object,
    }
    return render(request, 'company/companies_list.html', context)


# @user_passes_test(lambda u: u.option != '2')
# def company_update(request, pk):

#     user = request.user
#     try:
#         if user.is_superuser:
#             company = get_object_or_404(Company, pk=pk)
#         else:
#             company = get_object_or_404(Company, pk=user.company_id)

#         form = CompanyForm(instance=company)
#         if request.method == 'POST':
#             form = CompanyForm(
#                 request.POST or None, request.FILES or None, instance=company)

#             if form.is_valid():
#                 company = form.save(commit=True)
#                 messages.success(request, 'Dados alterados com sucesso!!!')
#                 if user.is_superuser:
#                     return redirect('company:companies_list')
#                 else:
#                     return redirect('company:company_update', user.company_id)

#             else:
#                 return render(request, 'company/company_update.html', {'form': form})

#         elif request.method == 'GET':
#             return render(request, 'company/company_update.html', {'form': form})

#     except:
#         return redirect('company:signup2')


@user_passes_test(lambda u: u.is_staff)
def company_agents_list(request):
    user = request.user
    form = User.objects.filter(company_id=user.company_id)
    template_name = 'company/company_users_list.html'

    context = {
        'form': form
    }
    return render(request, template_name, context)


@user_passes_test(lambda u: u.option != '2')
# @user_passes_test(lambda u: u.is_superuser)
def company_update(request, pk):
    
    user = request.user
    try:
        if user.is_superuser:
            company = get_object_or_404(Company, pk=pk)
        else:
            company = get_object_or_404(Company, pk=user.company_id)
        form = CompanyForm(instance=company)

        if request.method == 'POST':
            
            form = CompanyForm(request.POST, instance=company)            
            Formset_destiny_Factory = inlineformset_factory(Company, CompanyDestinies, fields=('destiny',), extra=1)        
            destiny_form = Formset_destiny_Factory(request.POST, instance=company)            
            Formset_phone_Factory = inlineformset_factory(Company, Phone, form=PhoneForm, extra=1)
            phone_form = Formset_phone_Factory(request.POST, instance=company)            
            Formset_social_Factory = inlineformset_factory(Company, SocialMedia, fields=('socmedia',), extra=1)        
            socmedia_form = Formset_social_Factory(request.POST, instance=company)

            if form.is_valid() and phone_form.is_valid() and socmedia_form.is_valid() and destiny_form.is_valid():
                company = form.save()
                destiny_form.save()
                phone_form.save()
                socmedia_form.save()
                messages.success(request, 'Dados alterados com sucesso!!!')
                return redirect('company:company_update', pk=pk)
                
            else:
                context = {
                    'form': form,
                    'formset_destiny' : destiny_form,
                    'formset_phone': phone_form,
                    'formset_socmedia': socmedia_form
                }
            return render(request, 'company/company_update.html', context)

        elif request.method == 'GET':
            
            form = CompanyForm(instance=company)            
            Formset_destiny_Factory = inlineformset_factory(Company, CompanyDestinies, fields=('destiny',), extra=1)        
            destiny_form = Formset_destiny_Factory(instance=company)            
            Formset_phone_Factory = inlineformset_factory(Company, Phone, form=PhoneForm, extra=1)
            phone_form = Formset_phone_Factory(instance=company)            
            Formset_social_Factory = inlineformset_factory(Company, SocialMedia, fields=('socmedia',), extra=1)        
            socmedia_form = Formset_social_Factory(instance=company)
            
            context = {
                'form': form,
                'formset_destiny' : destiny_form,
                'formset_phone': phone_form,
                'formset_socmedia': socmedia_form
            }
            return render(request, 'company/company_update.html', context)

    except:
        return redirect('company:signup2')


# def company_update(request, pk):
    
#     user = request.user
#     destiny_form = CompanyDestinies.objects.get(pk=pk)
#     try:
#         if user.is_superuser:
#             company = get_object_or_404(Company, pk=pk)
#         else:
#             company = get_object_or_404(Company, pk=user.company_id)
#         form = CompanyForm(instance=company)

#         if request.method == 'POST':
            
#             form = CompanyForm(request.POST, instance=company)            
#             destiny_form = get_object_or_404(CompanyDestinies, pk=user.company_id)
#             Formset_destiny_Factory = inlineformset_factory(Company, CompanyDestinies, fields=('destiny',), extra=1)        
#             destiny_form = Formset_destiny_Factory(request.POST, instance=company)            
#             Formset_phone_Factory = inlineformset_factory(Company, Phone, form=PhoneForm, extra=1)
#             phone_form = Formset_phone_Factory(request.POST, instance=company)            
#             Formset_social_Factory = inlineformset_factory(Company, SocialMedia, fields=('socmedia',), extra=1)        
#             socmedia_form = Formset_social_Factory(request.POST, instance=company)

#             if form.is_valid() and phone_form.is_valid() and socmedia_form.is_valid() and destiny_form.is_valid():
#                 company = form.save()
#                 destiny_form.save()
#                 phone_form.save()
#                 socmedia_form.save()
#                 messages.success(request, 'Dados alterados com sucesso!!!')
#                 return redirect('company:company_update', pk=pk)
                
#             else:
#                 context = {
#                     'form': form,
#                     'formset_destiny' : destiny_form,
#                     'formset_phone': phone_form,
#                     'formset_socmedia': socmedia_form
#                 }
#             return render(request, 'company/company_update.html', context)

#         elif request.method == 'GET':
            
#             form = CompanyForm(instance=company)            
#             Formset_destiny_Factory = inlineformset_factory(Company, CompanyDestinies, fields=('destiny',), extra=1)        
#             destiny_form = Formset_destiny_Factory(instance=company)            
#             Formset_phone_Factory = inlineformset_factory(Company, Phone, form=PhoneForm, extra=1)
#             phone_form = Formset_phone_Factory(instance=company)            
#             Formset_social_Factory = inlineformset_factory(Company, SocialMedia, fields=('socmedia',), extra=1)        
#             socmedia_form = Formset_social_Factory(instance=company)
            
#             context = {
#                 'form': form,
#                 'formset_destiny' : destiny_form,
#                 'formset_phone': phone_form,
#                 'formset_socmedia': socmedia_form
#             }
#             return render(request, 'company/company_update.html', context)

#     except:
#         return redirect('company:signup2')


# destiny_form = get_object_or_404(CompanyDestinies, pk=user.company_id)

class CompanyDestinyDeleteView(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    
    model = CompanyDestinies
    template_name = 'company/company_delete.html'
    success_url = _('company:company_list')
    success_message = 'Destino deletado com sucesso!'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request,self.success_message)
        return super(CompanyDestinyDeleteView, self).delete(request, *args, **kwargs)


company_delete = CompanyDestinyDeleteView.as_view()