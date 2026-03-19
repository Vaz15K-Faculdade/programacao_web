from .models import Categoria


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return dict(lista_categorias=categorias)
