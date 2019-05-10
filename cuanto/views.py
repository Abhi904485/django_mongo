from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView

from .models import Cuanto


# Create your views here.

class CuantoCreateView(CreateView):
    model = Cuanto
    fields = ['team_name', 'cuanto_url', 'db_ip', 'db_pass', 'db_user', 'db_port', 'db_name', 'db_connection_status']

    def get_success_url(self):
        return reverse('list')


class CuantoDetailView(DetailView):
    model = Cuanto


class CuantoListView(ListView):
    model = Cuanto


class CuantoDeleteView(DeleteView):
    model = Cuanto

    def get_success_url(self):
        return reverse('list')


class CuantoUpdateView(UpdateView):
    model = Cuanto
    fields = ['team_name', 'cuanto_url', 'db_ip', 'db_pass', 'db_user', 'db_port', 'db_name', 'db_connection_status']

    extra_context = {'update': 'update'}

    def get_success_url(self):
        return reverse('list')
