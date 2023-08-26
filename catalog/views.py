from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductVersionForm
from catalog.models import Product, ProductVersion


class ProductsCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')
    login_url = reverse_lazy('users:login')
    raise_exception = True

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductVersionFormset = inlineformset_factory(Product, ProductVersion, form=ProductVersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductVersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductVersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        form.instance.user = self.request.user
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.user


class ProductsListView(ListView):
    model = Product


class ProductsDetailView(DetailView):
    model = Product


class ProductsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')
    login_url = reverse_lazy('users:login')
    raise_exception = True

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.user
