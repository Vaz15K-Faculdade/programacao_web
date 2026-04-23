from django.shortcuts import render, redirect

from carrinho.models import Carrinho, CarItem
from produto.models import Produto


# Create your views here.
def visualizar_carinho(request, car_items=None, total=0, quantidade=0):
    try:
        carrinho = Carrinho.objects.get(car_id=_get_car_id(request))
        car_items = CarItem.objects.filter(car=carrinho, is_active=True)

        for item in car_items:
            total += item.produto.preco * item.quant
            quantidade += item.quant
    except Carrinho.DoesNotExist:
        pass

    context = {"car_items": car_items, "total": total, "quantidade": quantidade}
    return render(request, "loja/carrinho.html", context)


def _get_car_id(request):
    car = request.session.session_key
    if not car:
        car = request.session.create()
    return car


def adicionar_carrinho(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    try:
        car = Carrinho.objects.get(car_id=_get_car_id(request))
    except Carrinho.DoesNotExist:
        car = Carrinho.objects.create(car_id=_get_car_id(request))
        car.save()
    try:
        car_item = CarItem.objects.get(produto=produto, car=car)
        car_item.quant += 1
        car_item.save()
    except CarItem.DoesNotExist:
        car_item = CarItem.objects.create(produto=produto, quant=1, car=car)
        car_item.save()
    return redirect("carrinho")
