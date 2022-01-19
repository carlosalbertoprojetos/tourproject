from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render

from .forms import EditUserForm
from .models import User


def edit_user_view(request, pk):
    context = {}
    obj = get_object_or_404(User, pk=pk)
    form = EditUserForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+pk)

    context["form"] = form

    return render(request, "user/edit_user.html", context)


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

