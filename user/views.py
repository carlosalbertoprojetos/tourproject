from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
# from django.views.generic.edit import UpdateView

from .forms import EditUserForm
from .models import User

# class Signup2View(LoginRequiredMixin, CreateView):
#     model = Company
#     template_name = 'account/signup_2.html'
#     form_class = Signup2Form
#     success_url = reverse_lazy('user:dashboard')

#     def get_object(self):
#         self.object = self.request.user
#         return self.object

#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.user = self.request.user
#         obj.save()
#         return super().form_valid(form)


# signup_step_2 = Signup2View.as_view()


@user_passes_test(lambda u: u.is_superuser)
def list_users(request):
    object = User.objects.all()
    context = {
        'object': object,
    }

    return render(request, 'user/list_users.html', context)


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

    elif request.method == 'GET':
        return render(request, 'user/edit_user.html', {'form': form})


# @login_required
# def list_user_companies(request):
#     object = Company.objects.all()
#     context = {
#         'object': object,
#     }

#     return render(request, 'user/list_companies.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def list_user_companies_admin(request, pk):
#     object = Company.objects.filter(pk=pk)
#     context = {
#         'object': object,
#     }

#     return render(request, 'user/list_companies.html', context)


# class CompanyUserEditView(UpdateView):
#     model = Company
#     form_class = EditCompanyForm
#     template_name = 'user/edit_company.html'
#     success_url = reverse_lazy('user:dashboard')
#     success_message = 'Editado com sucesso!'


# edit_company_view = CompanyUserEditView.as_view()


# @login_required
# def edit_company_view(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     form = EditCompanyForm(instance=user)

#     if request.method == 'POST':
#         form = EditCompanyForm(request.POST or None,
#                                request.FILES, instance=user)

#         if form.is_valid():
#             user = form.save(commit=True)
#             return redirect('user:list_companies')
#         else:
#             return render(request, 'user/edit_company.html', {'form': form})

#     elif request.method == 'GET' :
#         return render(request, 'user/edit_company.html', {'form': form})
