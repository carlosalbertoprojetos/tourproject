from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EditUserForm
from .models import User


@user_passes_test(lambda u: u.is_superuser)
def users_list(request):
    object = User.objects.all()
    context = {
        'object': object,
    }

    return render(request, 'user/users_list.html', context)


@login_required
def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = EditUserForm(instance=user)
    if request.method == 'POST':
        form = EditUserForm(request.POST or None, request.FILES, instance=user)

        if form.is_valid():
            user = form.save(commit=True)
            return redirect('user:user_edit', user.pk)
        else:
            return render(request, 'user/user_edit.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'user/user_edit.html', {'form': form})
