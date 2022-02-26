from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as _
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import ProductForm
from .models import Categories, Products




class CategoryRegisterView(CreateView):
    model = Categories
    template_name = 'product/category_register.html'
    fields = '__all__'
    success_message = 'Categoria cadastrada com sucesso!!!'
    success_url = _('product:products_list')


category_register = CategoryRegisterView.as_view()


class ProductRegisterView(SuccessMessageMixin, CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'product/product_register.html'
    success_message = 'Produto cadastrado com sucesso!!!'
    success_url = _('product:products_list')


product_register = ProductRegisterView.as_view()


class ProductsListView(ListView):
    model = Products
    paginate_by = 4
    template_name = 'product/products_list.html'
    # template_name = 'product/products_list_dash.html'


products_list = ProductsListView.as_view()


class ProductsDetailView(DetailView):
    model = Products
    template_name = 'product/product_details.html'


product_details = ProductsDetailView.as_view()


class ProductUpdateView(UpdateView):
    model = Products
    form_class = ProductForm
    template_name = 'product/product_update.html'
    success_message = 'Produto atualizado com sucesso!!!'
    success_url = _('product:products_list')


product_update = ProductUpdateView.as_view()


# class ProductsDeleteView(DeleteView):
#     model = Products
#     template_name = 'products/products_delete.html'
#     success_url = reverse_lazy('produto:listar_produtos')

#     def delete(self, request, *args, **kwargs):
#         return super(ProductsDeleteView, self).delete(request, *args, **kwargs)


# product_delete = ProductsDeleteView.as_view()
