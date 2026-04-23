from django.db import models

from produto.models import Produto

# Create your models here.
class Carrinho(models.Model):
    car_id = models.CharField(max_length=250, unique=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.car_id

class CarItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    car = models.ForeignKey(Carrinho, on_delete=models.CASCADE, null=True)
    quant = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.produto