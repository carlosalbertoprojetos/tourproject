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
    obj = get_object_or_404(User, pk=pk)
    form = EditUserForm(instance=obj)
    user = request.user

    if request.method == 'POST':
        form = EditUserForm(request.POST or None, instance=obj)

        if form.is_valid():
            obj = form.save(commit=True)
            if user.is_superuser:
                return redirect('user:users_list')
            else:
                return redirect('user:user_edit', user.pk)
        else:
            return render(request, 'user/user_edit.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'user/user_edit.html', {'form': form})
