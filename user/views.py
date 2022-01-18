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
