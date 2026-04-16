from django.shortcuts import render

from produto.models import Produto


# Create your views here.
def visualizar_loja(request, categoria_slug=None):
    if categoria_slug:
        produtos = Produto.objects.filter(categoria__slug=categoria_slug)
    else:
        produtos = Produto.objects.all()

    context = {"produtos": produtos}
    return render(request, "loja/loja.html", context)

def produto_detalhe(request, categoria_slug, produto_slug):
    try:
        produto = Produto.objects.get(categoria__slug=categoria_slug, slug=produto_slug)
    except Exception as e:
        raise e

    context = {"produto": produto}
    return render(request, "detalhes_produto.html", context)
