from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from tm_global.models.mod_cad_global import Clientes, Fornecedores
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def home(request):
    # return render(request, "tmglobal/pages/hlogin.html")
    return render(request, "registration/login.html")


@login_required
def hp_corp(requests):
    return render(requests, "./pages/hp_corp.html")


# Classe para retornar todos os registros do cadastro de clientes
class ClientListViewBase(LoginRequiredMixin, ListView):
    model = Clientes
    context_object_name = "vwclientes"
    ordering = ["-cliente_pk"]
    template_name = "pages/hp_corp.html"
    paginate_by = 10

    def get_queryset(self):
        txt_nomecli = self.request.GET.get("nm_com_cli")
        if txt_nomecli:
            vclientes = Clientes.objects.filter(nm_com_cli__icontains=txt_nomecli)
        else:
            vclientes = Clientes.objects.all()
        return vclientes


# Classe para Visualizar cadastro de Cliente
class ClientViewBase(DetailView):
    model = Clientes
    template_name = "pages/hp_corp.html"
    success_url = reverse_lazy("glbclient")


# Classe para Inserir registros no cadastro de Clientes
class ClientCreatetBase(LoginRequiredMixin, CreateView):
    model = Clientes
    fields = [
        "cliente_pk",
        "emp_fil_fk_cli",
        "cnpj_cpf_cli",
        "fam_cad_cli",
        "tp_cli",
        "nm_jur_cli",
        "nm_com_cli",
        "tel_cli",
        "end_cli",
        "end_compl_cli",
        "end_bairro_cli",
        "end_cidade_cli",
        "end_cep_cli",
        "end_uf_cli",
        "dt_ini_relac_cli",
        "email_cli",
        "contato_cli",
        "ie_cli",
        "im_cli",
        "banco_cli",
        "agencia_cli",
        "ccorrente_cli",
        "tp_pag_cli",
        "lim_cred_cli",
        "venc_lim_cred_cli",
        "status_cad_cli",
    ]
    template_name = "pages/hp_corp.html"
    success_url = reverse_lazy("glbclient")


# Classe para Alterar registros no cadastro de Clientes
class ClientUpdatetBase(LoginRequiredMixin, UpdateView):
    model = Clientes
    fields = [
        "nm_jur_cli",
        "nm_com_cli",
        "status_cad_cli",
        "tp_cli",
        "fam_cad_cli",
        "tel_cli",
        "end_cli",
        "end_compl_cli",
        "end_bairro_cli",
        "end_cidade_cli",
        "end_cep_cli",
        "end_uf_cli",
        "dt_ini_relac_cli",
        "contato_cli",
        "email_cli",
        "ie_cli",
        "im_cli",
        "banco_cli",
        "agencia_cli",
        "ccorrente_cli",
        "tp_pag_cli",
        "lim_cred_cli",
        "venc_lim_cred_cli",
    ]
    template_name = "pages/hp_corp.html"
    success_url = reverse_lazy("glbclient")


# Classe para Delete de registros no cadastro de Clientes
class ClientDeletetBase(LoginRequiredMixin, DeleteView):
    model = Clientes
    template_name = "pages/hp_corp.html"
    success_url = reverse_lazy("glbclient")


# Classe para retornar todos os registros do cadastro de Fornecedores
class ForneceListViewBase(LoginRequiredMixin, ListView):
    model = Fornecedores
    context_object_name = "vwfornece"
    ordering = ["-fornece_pk"]
    template_name = "pages/hp_corp.html"
    paginate_by = 3

    def get_queryset(self):
        txt_nomefor = self.request.GET.get("nm_com_for")
        if txt_nomefor:
            vfornecedor = Fornecedores.objects.filter(nm_com_for__icontains=txt_nomefor)
        else:
            vfornecedor = Fornecedores.objects.all()
        return vfornecedor
