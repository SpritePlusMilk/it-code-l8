from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core import models


class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


def index(request):
    return render(request=request, template_name='core/index.html')


class ClientsList(ListView, TitleMixin):
    title = 'Список студентов'
    model = models.Client
    template_name = 'core/clients_list.html'
    context_object_name = 'clients'


class WebsitesList(ListView, TitleMixin):
    model = models.Website
    template_name = 'core/websites_list.html'
    context_object_name = 'websites'


class DetailClient(DetailView):
    title = 'студент № '
    model = models.Client
    template_name = 'core/client.html'
    context_object_name = 'client'


class DetailWebsite(DetailView):
    title = 'Сайт '
    model = models.Website
    template_name = 'core/website.html'
    context_object_name = 'website'


def clients_list(request):
    context = {'clients': models.Client.objects.all()}
    return render(request=request, template_name='core/clients_list.html',context=context)


def detail_client(request,id):
    context = {'client': models.Client.objects.get(id=id)}
    return render(request=request, template_name='core/client.html',context=context)



