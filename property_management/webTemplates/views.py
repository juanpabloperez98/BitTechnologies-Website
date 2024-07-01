from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from api.models import Property
from .form import PropertyForm
from django.urls import reverse_lazy
from django.conf import settings


class PropertyListView(ListView):
    model = Property
    template_name = "property_list.html"
    context_object_name = "properties"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_docker'] = settings.IS_DOCKER
        return context


class PropertyCreateView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = "property_form.html"
    success_url = reverse_lazy("property-list")


class PropertyUpdateView(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = "property_form.html"
    success_url = reverse_lazy("property-list")


class PropertyDeleteView(DeleteView):
    model = Property
    template_name = "property_confirm_delete.html"
    success_url = reverse_lazy("property-list")