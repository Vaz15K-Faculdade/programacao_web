from django.shortcuts import render
from categoria.models import Categoria
from produto.models import Produto


def home(request, categoria_slug=None):
    if categoria_slug:
        categoria = Categoria.objects.get(slug=categoria_slug)
        produtos = Produto.objects.filter(categoria=categoria)
    else:
        produtos = Produto.objects.all()

    context = {"produtos": produtos}
    return render(request, "home.html", context)
