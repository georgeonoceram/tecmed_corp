from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from tm_global.models.mod_tm_rat import RelAtTec


# Classe para retornar todos os registros do Rel.At.Técnico
class RatListViewBase(LoginRequiredMixin, ListView):
    model = RelAtTec
    context_object_name = "vwrat"
    ordering = ["-rat_pk"]
    template_name = "pages/hp_corp.html"
    paginate_by = 10

    def get_queryset(self):
        txt_ratcli = self.request.GET.get("desc_rat")
        if txt_ratcli:
            vrat = RelAtTec.objects.filter(desc_rat__icontains=txt_ratcli)
        else:
            vrat = RelAtTec.objects.all()
        return vrat


# Classe para Visualizar Rel.At.Técnico
class RatViewBase(DetailView):
    model = RelAtTec
    template_name = "pages/hp_corp.html"
    success_url = reverse_lazy("htmrat")


# Classe para Inserir registros Rel.At.Técnico
class RatCreatetBase(LoginRequiredMixin, CreateView):
    model = RelAtTec
    fields = [
        "rat_pk",
        "tp_rat",
        "dt_rat",
        "probl_rat",
        "desc_rat",
        "conclusao_rat",
        "desc_pecas_rat",
        "hr_ini_rat",
        "hr_fim_rat",
        "vl_atend_rat",
        "vl_pecas_rat",
    ]
    template_name = "pages/hp_corp.html"
    success_url = reverse_lazy("htmrat")


# Classe para Alterar registros Rel.At.Técnico
class RatUpdatetBase(LoginRequiredMixin, UpdateView):
    model = RelAtTec
    fields = [
        "probl_rat",
        "desc_rat",
        "conclusao_rat",
        "desc_pecas_rat",
        "vl_atend_rat",
        "vl_pecas_rat",
    ]
    template_name = "pages/hp_corp.html"
    success_url = reverse_lazy("htmrat")


# Classe para Delete de registros Rel.At.Técnico
class RatDeletetBase(LoginRequiredMixin, DeleteView):
    model = RelAtTec
    template_name = "pages/hp_corp.html"
    success_url = reverse_lazy("htmrat")
