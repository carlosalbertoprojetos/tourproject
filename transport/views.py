from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy as _
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .forms import (
    TransportCategoryPaxForm,
    TransportForm,
    TransportTypeForm,
    TransportPriceForm,
)
from .models import Transport, Transport_Type, TransportCategoryPax, TransportPrices


class TransportCategoryListCreateView(
    LoginRequiredMixin, SuccessMessageMixin, ListView
):
    model = Transport_Type
    template_name = "transport/transport_category_list_create.html"

    def get_context_data(self, **kwargs):
        context = super(TransportCategoryListCreateView, self).get_context_data(
            **kwargs
        )
        context["form"] = TransportTypeForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TransportTypeForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Categoria de Transporte criada com sucesso!!!")
            return redirect("transport:transport_category_list_create")
        else:
            return render(
                request,
                "transport/transport_category_list_create.html",
                {"object": "object", "form": form},
            )


transport_category_list_create = TransportCategoryListCreateView.as_view()


class TransportCategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Transport_Type
    form_class = TransportTypeForm
    template_name = "transport/transport_category_update.html"
    success_message = "Categoria de Transporte alterada com sucesso!!!"
    success_url = _("transport:transport_category_list_create")


transport_category_update = TransportCategoryUpdateView.as_view()


class TransportCategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Transport_Type
    template_name = "transport/transport_category_delete.html"
    success_message = "Categoria de Transporte deletada com sucesso!!!"
    success_url = _("transport:transport_category_list_create")

    def delete(self, request, *args, **kwargs):
        return super(TransportCategoryDeleteView, self).delete(request, *args, **kwargs)


transport_category_delete = TransportCategoryDeleteView.as_view()


class TransportCategoryPaxListCreateView(
    LoginRequiredMixin, SuccessMessageMixin, ListView
):
    model = TransportCategoryPax
    template_name = "transport/transport_catpax_list_create.html"

    def get_context_data(self, **kwargs):
        context = super(TransportCategoryPaxListCreateView, self).get_context_data(
            **kwargs
        )
        context["form"] = TransportCategoryPaxForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TransportCategoryPaxForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(
                request, "Categoria PAX de Transporte criada com sucesso!!!"
            )
            return redirect("transport:transport_catpax_list_create")
        else:
            return render(
                request,
                "transport/transport_catpax_list_create.html",
                {"object": "object", "form": form},
            )


transport_catpax_list_create = TransportCategoryPaxListCreateView.as_view()


class TransportCategoryPaxUpdateView(
    LoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    model = TransportCategoryPax
    form_class = TransportCategoryPaxForm
    template_name = "transport/transport_catpax_update.html"
    success_message = "Categoria PAX de Transporte alterada com sucesso!!!"
    success_url = _("transport:transport_catpax_list_create")


transport_catpax_update = TransportCategoryPaxUpdateView.as_view()


class TransportCategoryPaxDeleteView(
    LoginRequiredMixin, SuccessMessageMixin, DeleteView
):
    model = TransportCategoryPax
    template_name = "transport/transport_catpax_delete.html"
    success_message = "Categoria PAX de Transporte deletada com sucesso!!!"
    success_url = _("transport:transport_catpax_list_create")

    def delete(self, request, *args, **kwargs):
        return super(TransportCategoryPaxDeleteView, self).delete(
            request, *args, **kwargs
        )


transport_catpax_delete = TransportCategoryPaxDeleteView.as_view()


class TransportListCreateView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Transport
    template_name = "transport/transport_list_create.html"

    def get_context_data(self, **kwargs):
        context = super(TransportListCreateView, self).get_context_data(**kwargs)
        context["form"] = TransportForm(self.request.POST or None, self.request.FILES)
        return context

    def post(self, request, *args, **kwargs):
        form = TransportForm(request.POST or None, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Transporte criado com sucesso!!!")
            return redirect("transport:transport_list_create")
        else:
            return render(
                request,
                "transport/transport_list_create.html",
                {"object": "object", "form": form},
            )


transport_list_create = TransportListCreateView.as_view()


class TransportUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Transport
    form_class = TransportForm
    template_name = "transport/transport_update.html"
    success_message = "Dados alterados com sucesso!!!"
    success_url = _("transport:transport_list_create")


transport_update = TransportUpdateView.as_view()


class DeletarTransporteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Transport
    template_name = "transport/transport_delete.html"
    success_url = _("transport:transport_list_create")
    success_message = "Deletado com sucesso!"

    def delete(self, request, *args, **kwargs):
        return super(DeletarTransporteView, self).delete(request, *args, **kwargs)


transport_delete = DeletarTransporteView.as_view()


class TransporPricetListView(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = TransportPrices
    form_class = TransportPriceForm
    template_name = "transport/transport_price_list_create.html"

    def get_context_data(self, **kwargs):
        context = super(TransporPricetListView, self).get_context_data(**kwargs)
        context["form"] = TransportPriceForm(self.request.POST or None)
        return context

    def post(self, request, *args, **kwargs):
        form = TransportPriceForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Valor de Transporte criado com sucesso!!!")
            return redirect("transport:transport_price_list_create")
        else:
            return render(
                request,
                "transport/transport_price_list_create.html",
                {"object": "object", "form": form},
            )


transport_price_list_create = TransporPricetListView.as_view()


class TransportPriceUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = TransportPrices
    form_class = TransportPriceForm
    template_name = "transport/transport_price_update.html"
    success_message = "Valor de Transporte atualizado com sucesso!!!"
    success_url = _("transport:transport_price_list_create")


transport_price_update = TransportPriceUpdateView.as_view()


class TransportPriceDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = TransportPrices
    template_name = "transport/transport_price_delete.html"
    success_message = "Valor de Transporte deletado com sucesso!!!"
    success_url = _("transport:transport_price_list_create")

    def delete(self, request, *args, **kwargs):
        return super(TransportPriceDeleteView, self).delete(request, *args, **kwargs)


transport_price_delete = TransportPriceDeleteView.as_view()
