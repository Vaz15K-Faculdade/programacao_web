from django.shortcuts import render
from produto.models import Produto


def home(request):
    produtos = Produto.objects.all()
    context = {"produtos": produtos}
    return render(request, "home.html", context)
