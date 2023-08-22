from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def home(request):
    # return render(request, "tmglobal/pages/hlogin.html")
    return render(request, "registration/login.html")


@login_required
def hcorp(requests):
    return render(requests, "tmglobal/pages/hcorp.html")