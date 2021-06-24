from django.urls.base import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    DeleteView,
    CreateView,
    UpdateView,
    DetailView,
)

from .models import Snack

# Create your views here.
class SnackListView(ListView):
    model = Snack
    template_name = "snack_list.html"


class SnackDetailView(DetailView):
    model = Snack
    template_name = "snack_detail.html"


class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["name", "purchaser", "description"]


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["name", "purchaser", "description"]


class SnackDeleteView(DeleteView):
    model = Snack
    template_name = "snack_delete.html"
    success_url = reverse_lazy("snack_list")
